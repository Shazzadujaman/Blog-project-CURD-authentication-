from django.db import models
from catagories.models import Catagories
from author.models import Author

# Create your models here.
class Post(models.Model):
    title=models.CharField()
    content=models.TextField()
    catagory=models.ManyToManyField(Catagories)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
     return f"{self.title}"