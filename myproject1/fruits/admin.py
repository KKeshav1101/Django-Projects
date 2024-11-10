from django.contrib import admin
from fruits.models import FruitsInfo,FruitsVendors
# Register your models here.
admin.site.register(FruitsVendors)
admin.site.register(FruitsInfo)
