from django.db import models

# Create your models here.
from distutils.command.upload import upload
from tkinter import Image
from django.db import models

# Create your models here.
class slider(models.Model):
    DISCOUNT_DEAL = (
        ('HOT DEALS','HOT DEALS'),
        ('NEW ARRAIVELS','NEW ARRAIVELS'),
        
    )

    Image = models.ImageField(upload_to='media/slider_imgs')
    Discount_Deal = models.CharField(choices=DISCOUNT_DEAL, max_length=100)
    SALE = models.IntegerField()
    Brand_Name = models.CharField(max_length=200)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=500)

    def __str__(self):
        return self.Brand_Name

class BannerAreas(models.Model):
    Images = models.ImageField(upload_to='media/banner_imgs')
    Discount_Deal = models.CharField(max_length=100)
    Quote = models.CharField(max_length=200)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=500, null=True)
    def __str__(self):
        return self.Quote

class MainCatagory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name 

class Catagory(models.Model):
    name = models.CharField(max_length=100)
    mainCatagory = models.ForeignKey(MainCatagory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + '--' + self.mainCatagory.name

class SubCatagory(models.Model):
    Catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name