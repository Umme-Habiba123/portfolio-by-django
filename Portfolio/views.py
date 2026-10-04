from django.shortcuts import render, redirect
from .models import *
from .forms import *

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password


User=get_user_model()


# Create your views here.

def home(request):
    portfolio=Portfolio.objects.all()
    
    return render(request, 'home.html',{
        'portfolio' : portfolio
    })
    
    
def about(request):
    return render(request, 'about.html')


def registration(request):
    if request.method =='POST':
       form = RegistrationForm(request.POST)
       if form.is_valid():
        password=form.cleaned_data.get('password1')
        user=form.save(commit=False)
        user.save()
        return redirect('login')
    else:
        form=RegistrationForm()
        
    return render(request, 'registration.html',{
        form: form
    })
    
def login(request):
    if request.method=='POST':
        form =LoginForm(request, data=request.POST)
        
        if form.is_valid():
            
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            
        user=authenticate(username=username, password=password)
        
        if user:
            login(request,user)
            return redirect('home.html')
    
    else:
        form= LoginForm()
        
    return render(request, 'loginform.html',{
        'form':form
    })