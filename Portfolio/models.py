from django.db import models

# Create your models here.

class Portfolio(models.Model):
    name=models.CharField(max_length=200)
    # profile=models.ImageField(upload_to='profile/')
    bio=models.CharField(max_length=200)
    email=models.CharField(max_length=25)
    phone=models.CharField(max_length=20)
    location=models.CharField(max_length=100)
    skills=models.CharField(max_length=200)
    projects=models.CharField(max_length=200)
    
    
    def __str__(self):
        return f"{self.name}"
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
