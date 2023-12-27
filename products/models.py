from typing import Iterable, Optional
from django.db import models

# Create your models here.


class Address(models.Model):
    street = models.CharField(max_length=1024,null=True )
    zipCode = models.SlugField(null=True)
    city = models.PositiveIntegerField (null=True)
    country = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.title}"


class Brand(models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField(blank=True,)
    address = models.OneToOneField(Address,on_delete=models.DO_NOTHING,null=True,related_name="Products")

    def __str__(self):
        return f"{self.title}"
    

class Category(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.title}"


class Products(models.Model):
    title = models.CharField(max_length=70, blank=True)
    description = models.TextField(blank=True)
    brand = models.ForeignKey(Brand ,on_delete= models.CASCADE, null=True)
    image = models.ImageField(blank=True ,upload_to="product-img")
    category = models.ManyToManyField(Category)
    price = models.PositiveIntegerField()
    slug = models.SlugField(blank=True)
    is_best_seller = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title}"
    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = self.id
        super().save(*args, **kwargs)

class Feedback(models.Model):
    name = models.CharField(max_length=40)
    rating = models.PositiveIntegerField()
    products = models.ForeignKey(Products,on_delete=models.CASCADE)
    text = models.TextField()
    def __str__(self):
        return f"{self.products} -Rating {self.rating}" 
    