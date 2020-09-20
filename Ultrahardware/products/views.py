from django.shortcuts import render
from products import models as product_models

# Create your views here.


def Product(request, _product_id):
    category_parents = product_models.Category_parent.objects.order_by("order")
    context = {
        "category_parents": category_parents
    }
    return render(request, "products/Product.html", context)