from django.db import models
from django.contrib import admin
class product(models.Model):
    name=models.CharField(max_length=100)
    product_id=models.IntegerField(primary_key=True)
    brand=models.CharField(max_length=20)
    price=models.FloatField()
    manufacture_date=models.DateField()
    expiry_date=models.DateField()
    warranty=models.CharField(max_length=10)
class productAdmin(admin.ModelAdmin):
    list_display=["name","product_id","brand","price","manufacture_date","expiry_date","warranty"]