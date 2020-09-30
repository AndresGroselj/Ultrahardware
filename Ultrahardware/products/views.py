from django.shortcuts import render
from . import models

# Create your views here.


def Product(request, _product_id):
    category_parents = models.Category_parent.objects.order_by("order")
    context = {
        "category_parents": category_parents
    }
    return render(request, "products/Product.html", context)

def Popular(request):
    category_parents = models.Category_parent.objects.order_by("order")
    products = models.Product.objects.order_by("views")[::-1]
    context = {   
        "products": products,
        "category_parents": category_parents
    }
    return render(request, "products/PopularProducts.html", context)