from django.db import models
from categories.models import Categories
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField()
    content=models.TextField()
    category=models.ManyToManyField(Categories)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
     return f"{self.title}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"