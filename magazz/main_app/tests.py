from django.test import TestCase
from .models import Product, Category, Review
import datetime


class ProductTestCase(TestCase):
    def setUp(self):
        cat = Category.objects.create(title="test_cat")
        Product.objects.create(name="test_prod",
                               photo="test.jpg",
                               descript="testdescr",
                               price=666,
                               category=cat,
                               publishdate="2017-11-05")

    def test_product_created(self):
        """Animals that can speak are correctly identified"""
        testobj = Product.objects.get(name="test_prod")
        self.assertEqual(testobj.photo, "test.jpg")
        self.assertEqual(testobj.descript, "testdescr")
        self.assertEqual(testobj.price, 666)
        self.assertEqual(testobj.category, Category.objects.get(title="test_cat"))
        self.assertEqual(testobj.publishdate, datetime.date(2017, 11, 5))


class ReviewTestCase(TestCase):
    def setUp(self):
        cat = Category.objects.create(title="test_cat")
        prod = Product.objects.create(name="test_prod",
                               photo="test.jpg",
                               descript="testdescr",
                               price=666,
                               category=cat,
                               publishdate="2017-11-05")
        Review.objects.create(username="testuser",
                              rewiewtext="some review text",
                              rate=3,
                              product=prod)

    def test_rewiew_created(self):
        """Animals that can speak are correctly identified"""
        testobj = Review.objects.get(username="testuser")
        self.assertEqual(testobj.rewiewtext, "some review text")
        self.assertEqual(testobj.rate, 3)
        self.assertEqual(testobj.product, Product.objects.get(name="test_prod"))
