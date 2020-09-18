from django.shortcuts import render
from products import models as product_models

# Create your views here.


def Home(request):
    categorie_parents = product_models.Category_parent.objects.order_by("order")
    products = product_models.Product.objects.all()
    context = {   
        "products": products,
        "jsonProducts": product_models.productsToJson(products),
        "categorie_parents": categorie_parents
    }
    return render(request, "Home.html", context)