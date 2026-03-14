from django.db import models

# Create your models here.
class Catagories(models.Model):
    name=models.CharField()
    

    def __str__(self):
        return f"{self.name}"