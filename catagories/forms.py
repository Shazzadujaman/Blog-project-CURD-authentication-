from django import forms
from . import models

class Catagories_form(forms.ModelForm):
    class Meta:
        model=models.Catagories
        fields='__all__'
        