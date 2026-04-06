from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class RegistrationForm(UserCreationForm):
    first_name=forms.CharField()
    last_name=forms.CharField()
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']


class EditProfile(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']

