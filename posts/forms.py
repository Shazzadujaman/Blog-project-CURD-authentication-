from django import forms
from . import models

class Post_form(forms.ModelForm):
    class Meta:
        model=models.Post
        fields=['title', 'content', 'category']
<<<<<<< HEAD

class CommentForm(forms.ModelForm):
    class Meta:
        model=models.Comment
        fields=['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...', 'class': 'form-control'}),
        }

        
=======
        
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
>>>>>>> abdfa808ff13bfb59dc6fe4fc61a6cb9fe1b8fbb
