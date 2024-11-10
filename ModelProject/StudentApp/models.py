from django.db import models

# Create your models here.
from django.db import models
class stud(models.Model):
    S_name=models.CharField(max_length=30)
    S_regno=models.IntegerField()
    S_M1=models.FloatField()
    S_M2=models.FloatField()
