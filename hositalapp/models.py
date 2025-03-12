from django.db import models

# Create your models here.
class patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    message = models.TextField()

    def __str__(self):
        return self.name


class doctor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    department = models.CharField(max_length=24)
    status = models.CharField(max_length=25)
    phone = models.CharField(max_length=24)

    def __str__(self):
        return self.name + " " + self.status


class staff(models.Model):
    firstname = models.CharField(max_length=24)
    lastname = models.CharField(max_length=24)
    position = models.CharField(max_length=24)
    phonenumber = models.CharField(max_length=24)
    email = models.EmailField()
    hiredate = models.DateField()

    def __str__(self):
        return self.firstname + " " + self.lastname

class ward(models.Model):
    name = models.CharField(max_length=24)
    totalbeds = models.IntegerField()
    availablebeds = models.IntegerField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=24)
    email = models.EmailField()
    phone = models.CharField(max_length=24)
    date = models.DateTimeField()
    department = models.CharField(max_length=24)
    doctor = models.CharField(max_length=24)
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=24)
    email = models.EmailField()
    subject = models.CharField(max_length=24)
    message = models.TextField()

    def __str__(self):
        return self.name+ " " +self.email


#Mpesa API
class Transaction(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount} - {self.status}"
