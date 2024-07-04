from django.db import models

# Create your models here.


class Register(models.Model):
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    username=models.CharField(max_length=30,null=True)
    password=models.CharField(max_length=20,null=True)
    email = models.EmailField(max_length=30, null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.username

class Product(models.Model):
    prdct_name= models.CharField(max_length=30,null=True)
    price=models.IntegerField(null=True)
    descriprion=models.CharField(max_length=30,null=True)


    def __str__(self):
        return self.prdct_name