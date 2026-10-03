from django.db import models

# Create your models here.

class Portfolio(models.Model):
    name=models.CharField(max_length=200)
    profile=models.ImageField(upload_to='profile/')
    bio=models.CharField(max_length=200)
    email=models.CharField(max_length=25)
    phone=models.IntegerField(max_length=20)
    location=models.CharField(max_length=100)
    skills=models.CharField(max_length=200)
    
    
    def __str__(self):
        return f"{self.name}"