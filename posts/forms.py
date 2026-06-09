from django import forms
from . import models

class Post_form(forms.ModelForm):
    class Meta:
        model=models.Post
        fields=['title', 'content', 'category']

class CommentForm(forms.ModelForm):
    class Meta:
        model=models.Comment
        fields=['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...', 'class': 'form-control'}),
        }

        