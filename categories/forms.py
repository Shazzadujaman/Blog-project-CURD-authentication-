from django import forms
from . import models

class Categories_form(forms.ModelForm):
    class Meta:
        model=models.Categories
        fields=['name']
        