from django.db import models
from categories.models import Categories
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField()
    content=models.TextField()
    category=models.ManyToManyField(Categories)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
     return f"{self.title}"
    

class Comment(models.Model):
   post=models.ForeignKey("Post", on_delete=models.CASCADE,related_name='comments')
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   content = models.TextField()
