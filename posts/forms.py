from django import forms
from . import models

class Post_form(forms.ModelForm):
    class Meta:
        model=models.Post
        fields=['title', 'content', 'category']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=models.Comment
        fields=['content'] 
        labels = {
            'content': 'Comment'
        }
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 2,   # 👈 reduce height
                'class': 'form-control'
            })
        }       
