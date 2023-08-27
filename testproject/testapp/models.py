from django.db import models




class SampleData(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=111)
    email=models.CharField(max_length=100)
    phone=models.IntegerField(default=0)
    address=models.CharField(max_length=210)