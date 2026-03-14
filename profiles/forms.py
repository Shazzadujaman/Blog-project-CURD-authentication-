from django import forms
from . import models

class profile_form(forms.ModelForm):
    class Meta:
        model=models.Profile
        fields='__all__'
        