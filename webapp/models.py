from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)
    password = models.CharField(max_length=50)

class Admin(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Cat(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    details = models.TextField()

class Photo(models.Model):
    catname = models.ForeignKey(Cat, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='webapp/static/images')
    caption = models.CharField(max_length=255, blank=True)

class MedicalRecord(models.Model):
    catname = models.ForeignKey(Cat, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    veterinarian = models.CharField(max_length=255)
    diagnosis = models.TextField()
    treatment_plan = models.TextField(blank=True)
    medication_prescribed = models.TextField(blank=True)
    next_appointment = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)

