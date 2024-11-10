from django.db import models

# Create your models here.
class Player(models.Model):
    firstname=models.CharField(max_length=15)
    lastname=models.CharField(max_length=15)
    dob=models.DateField()
    age=models.IntegerField()
    position=models.CharField(max_length=3)
    country=models.CharField(max_length=15)

