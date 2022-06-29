from django.db import models

# Create your models here.

class Movie(models.Model):  
    title = models.CharField(max_length=250)
    description = models.TextField()
    rating = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
