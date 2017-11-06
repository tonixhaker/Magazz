from django.test import TestCase
from .models import Product, Category, Review, Cart
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
        testobj = Review.objects.get(username="testuser")
        self.assertEqual(testobj.rewiewtext, "some review text")
        self.assertEqual(testobj.rate, 3)
        self.assertEqual(testobj.product, Product.objects.get(name="test_prod"))


class CategoryTestCase(TestCase):
    def setUp(self):
        cat = Category.objects.create(title="test_cat")

    def test_cat_created(self):
        testobj = Category.objects.get(title="test_cat")
        self.assertEqual(testobj.title, "test_cat")


class CartTestCase(TestCase):
    def setUp(self):
        cat = Category.objects.create(title="test_cat")
        prod = Product.objects.create(name="test_prod",
                                      photo="test.jpg",
                                      descript="testdescr",
                                      price=666,
                                      category=cat,
                                      publishdate="2017-11-05")
        Cart.objects.create(product=prod, quantity=666)

    def test_cart_created(self):
        testobj = Cart.objects.get(product=Product.objects.get(name="test_prod"))
        self.assertEqual(testobj.quantity, 666)


