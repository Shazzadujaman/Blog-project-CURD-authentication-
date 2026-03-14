from django import forms
from . import models

class Author_form(forms.ModelForm):
    class Meta:
        model=models.Author
        fields='__all__'
        