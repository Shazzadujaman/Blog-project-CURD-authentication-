from django import forms
from . import models

class Post_form(forms.ModelForm):
    class Meta:
        model=models.Post
        fields='__all__'
        