from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname=models.CharField(max_length=20,default="enter your first name here")
    lastname=models.CharField(max_length=20,verbose_name='surname',blank=True)
    address=models.CharField(max_length=20)