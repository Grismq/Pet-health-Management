from django.db import models

# Create your models here.
class PetHealthMonitoring(models.Model):
    AnimalName=models.CharField(max_length=500)
    Symptoms_1=models.CharField(max_length=500)
    Symptoms_2=models.CharField(max_length=500)
    Symptoms_3=models.CharField(max_length=500)
    Symptoms_4=models.CharField(max_length=500)
    Symptoms_5=models.CharField(max_length=500)
    Dangerous=models.CharField(max_length=500)

class PetAdoption(models.Model):
    pet_image=models.ImageField(upload_to="Pet")
    pet_name=models.CharField(max_length=400)
    pet_price=models.FloatField()
    address=models.TextField()
    contact_no=models.CharField(max_length=900)
