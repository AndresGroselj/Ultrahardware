from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "accounts"

urlpatterns = [
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
]