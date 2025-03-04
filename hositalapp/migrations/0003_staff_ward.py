# Generated by Django 5.1.6 on 2025-02-27 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hositalapp', '0002_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=24)),
                ('lastname', models.CharField(max_length=24)),
                ('position', models.CharField(max_length=24)),
                ('phonenumber', models.CharField(max_length=24)),
                ('email', models.EmailField(max_length=254)),
                ('hiredate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('totalbeds', models.IntegerField()),
                ('availablebeds', models.IntegerField()),
            ],
        ),
    ]
