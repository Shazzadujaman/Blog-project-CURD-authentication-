from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class RegistrationForm(UserCreationForm):
    first_name=forms.CharField()
    last_name=forms.CharField()
    role = forms.ChoiceField(
        choices=[
            ('super_admin', 'Super Admin'),
            ('moderator', 'Moderator'),
            ('author', 'Author'),
        ],
        required=True,
        initial='author'
    )
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']


class EditProfile(UserChangeForm):
    password=None
    role = forms.ChoiceField(
        choices=[
            ('super_admin', 'Super Admin'),
            ('moderator', 'Moderator'),
            ('author', 'Author'),
        ],
        required=True
    )
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and hasattr(self.instance, 'profile'):
            self.fields['role'].initial = self.instance.profile.role


