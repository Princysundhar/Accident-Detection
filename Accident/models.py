from django.db import models

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

class User(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    house_name = models.CharField(max_length=100)
    place = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)

    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE,default=1)

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    place = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    lattitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)

    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE, default=1)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)

    HOSPITAL = models.ForeignKey(Hospital,on_delete=models.CASCADE,default=1)

class Fecility(models.Model):
    fecility_type = models.CharField(max_length=100)
    details = models.CharField(max_length=100,default=1)

    HOSPITAL = models.ForeignKey(Hospital, on_delete=models.CASCADE, default=1)

class Police_station(models.Model):
    station_name = models.CharField(max_length=100)
    place = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    lattitude = models.CharField(max_length=100,default=1)
    longitude = models.CharField(max_length=100,default=1)

    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE, default=1)

class Accident(models.Model):
    lattitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=50)
    place = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    USER = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

class Report(models.Model):
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    ACCIDENT = models.ForeignKey(Accident,on_delete=models.CASCADE,default=1)
    HOSPITAL = models.ForeignKey(Hospital, on_delete=models.CASCADE, default=1)

