from django.shortcuts import render, redirect
from products import models as product_models

# Create your views here.


def Index(request):
    category_parents = product_models.Category_parent.objects.order_by("order")
    products = product_models.Product.objects.all()
    context = {   
        "products": products,
        "category_parents": category_parents
    }
    return render(request, "Index.html", context)

def Location(request):
    context = {
        "maps_key": "AIzaSyASverDnv0d0AigXo8nAmVeN9QXNcI2snU",
        "direccion": "Padre+Mariano+356,+Providencia,+Región+Metropolitana,Chile"
    }
    return render(request, "Location.html", context)
