from django.db import models

# Create your models here.

class Movies(models.Model):
   # movieId = models.PrimaryKey()
    movieName = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    seats = models.IntegerField(default=0)
    imgUrl=models.CharField(max_length=1000)
    
