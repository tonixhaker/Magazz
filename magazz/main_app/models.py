from django.db import models
import datetime


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='prod_img', blank=True)
    descript = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publishdate = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name


class Review(models.Model):
    username = models.CharField(max_length=100)
    rewiewtext = models.TextField()
    rate = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


