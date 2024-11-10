from django.db import models

# Create your models here.
class Faculty(models.Model):
    name=models.CharField(max_length=30)
    fid=models.IntegerField()
    dept=models.CharField(max_length=10)
    #fields=models.CharField(max_length=20)


