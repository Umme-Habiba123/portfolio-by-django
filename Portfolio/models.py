from django.db import models
from django.conf import settings

# Create your models here.

class Portfolio(models.Model):
    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='portfolios',
    null=True,
    blank=True
    )
    name=models.CharField(max_length=200)
    # profile=models.ImageField(upload_to='profile/')
    bio=models.CharField(max_length=200)
    email=models.CharField(max_length=25)
    phone=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    skills=models.CharField(max_length=300)
    projects=models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    
    
    def __str__(self):
        return f"{self.name}"
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return self.name
    

class AdditionalInfo(models.Model):
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
        related_name='additional_infos'
    )
    field_name = models.CharField(max_length=100)
    value = models.TextField()

    def __str__(self):
        return self.field_name


