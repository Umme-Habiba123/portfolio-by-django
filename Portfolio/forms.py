from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm



class PortfolioForm(forms.ModelForm):
     class Meta: 
         model= Portfolio
         fields='__all__'
         
         
class RegistrationForm( UserCreationForm):
    username=forms.CharField(label='username', 
     widget=forms.TextInput(
      attrs={
          'class':'form-control',
          'placeholder':'Input Username'
      }                           
                             ))
    
    email=forms.CharField(label='Email',
                          widget=forms.TextInput(
                              attrs={
                                  'class':'form-control',
                                  'placeholder':'Input Email'
                              }
                          ))
    
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(
         attrs={
             'class':'form-control',
             'placeholder':'Input Password'
         }
     ))
    
    password2=forms.CharField(label='Password',widget=forms.PasswordInput(
         attrs={
             'class':'form-control',
             'placeholder':'Input Password'
         }
     ))
    
class LoginForm(AuthenticationForm):
   
   username=forms.CharField(label='Username',
    widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Input Username'
        }
    ))
   password=forms.CharField(label='Password',
    widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Input Password'
        }
    ))
   
    # class Meta :
    #     model=Portfolio
    #     fields=['username','password']