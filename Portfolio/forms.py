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
    widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Input Password'
        }
    ))
   

from django import forms
from .models import Portfolio, ContactMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Input Email'
        })
    )

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username or Email',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Input Username or Email'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Input Password'
        })
    )


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Message',
                'rows': 4
            }),
        }
