from django.db import models

# Create your models here.
class contactUs(models.Model):
    Name=models.CharField( max_length=50,null=True)
    Surname=models.CharField( max_length=50 ,null=True)
    Email=models.CharField( max_length=50,null=True,unique=True)
    Message=models.TextField(null=True)