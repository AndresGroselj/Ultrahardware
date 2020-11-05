from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import Signup, Login, Logout
from django.contrib.auth import views as auth_views

# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_Signup(self):
        url = reverse("accounts:signup")
        self.assertEqual(resolve(url).func, Signup)
    
    def test_Login(self):
        url = reverse("accounts:login")
        self.assertEqual(resolve(url).func, Login)
    
    def test_Logout(self):
        url = reverse("accounts:logout")
        self.assertEqual(resolve(url).func, Logout)