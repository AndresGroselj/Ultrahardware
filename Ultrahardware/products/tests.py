from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import Product, Popular, List, Edit, Add

# Create your tests here.


class TestUrls(SimpleTestCase):
    def test_product(self):
        url = reverse("products:product", kwargs={'_product_id':1})
        self.assertEqual(resolve(url).func, Product)

    def test_popular(self):
        url = reverse("products:popular")
        self.assertEqual(resolve(url).func, Popular)
    
    def test_List(self):
        url = reverse("products:list")
        self.assertEqual(resolve(url).func, List)

    def test_edit(self):
        url = reverse("products:edit", kwargs={'_product_id':1})
        self.assertEqual(resolve(url).func, Edit)

    def test_add(self):
        url = reverse("products:add")
        self.assertEqual(resolve(url).func, Add)