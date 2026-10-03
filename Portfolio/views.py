from django.shortcuts import render
from .models import *
from .models import Portfolio

# Create your views here.

def home(request):
    portfolio=Portfolio.objects.all()
    
    return render(request, 'home.html',{
        'portfolio' : portfolio
    })
    