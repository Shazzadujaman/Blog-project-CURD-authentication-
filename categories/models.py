from django.db import models

# Create your models here.
class Categories(models.Model):
    name=models.CharField()
    slug=models.SlugField(unique=True, null=True, blank=True)
    

    def __str__(self):
        return f"{self.name}"