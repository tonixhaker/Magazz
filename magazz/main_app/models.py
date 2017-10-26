from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=300)
    photo = models.ImageField()
    descript = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Review(models.Model):
    username = models.CharField(max_length=100)
    rewiewtext = models.TextField()
    rate = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


