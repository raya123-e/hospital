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

