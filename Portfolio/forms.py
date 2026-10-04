from django import forms
from .models import *
from django.contrib.auth.forms import UserChangeForm


class PortfolioForm(forms.ModelForm):
     class Meta: 
         model= Portfolio
         fields='__all__'
         
         
class RegistrationForm(UserChangeForm):
    username=forms.CharField(label='username', 
     widget=forms.TextInput(
      attrs={
          'class':'form-control',
          'placeholder':'Input Username'
      }                           
                             ))
    
    email=forms.CharField(label='password',
                          widget=forms.PasswordInput(
                              attrs={
                                  'class':'form-control',
                                  'placeholder':'Input Password'
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
    
class LoginForm():
   
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