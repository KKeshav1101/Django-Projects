from django.db import models

# Create your models here.
class FruitsInfo(models.Model):
    name=models.CharField(max_length=30)
    origin=models.CharField(max_length=60)
    price=models.DecimalField(max_digits=4,null=False,decimal_places=2)
    availability=models.IntegerField(default=0)
    def __str__(self):
        return self.origin+" "+self.name

class FruitsVendors(models.Model):
    vendor_id=models.CharField(max_length=4,null=False,primary_key=True)
    vendor_name=models.CharField(max_length=60)
    vendor_location=models.CharField(max_length=60)
    def __str__(self):
        return self.vendor_id+"-"+self.vendor_name+"-"+self.vendor_location