from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "products"

urlpatterns = [
    path("popular/", views.Popular, name="popular"),
    path("<int:_product_id>/", views.Product, name="product"),
]