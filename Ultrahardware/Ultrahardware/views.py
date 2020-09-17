from django.shortcuts import render
from products import models as product_models

# Create your views here.


def Home(request):
    products = product_models.Product.objects.all()
    context = {   
        "products": products 
    }
    return render(request, "Home.html", context)