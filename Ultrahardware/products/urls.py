from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "products"

urlpatterns = [
    path("<int:_product_id>/", views.Product, name="product"),
    path("popular/", views.Popular, name="popular"),
    path("list/", views.List, name="list"),
    path("list/<int:_product_id>", views.Edit, name="edit"),
    path("list/add", views.Add, name="add"),
]