from django.shortcuts import render
from . import models
from . import forms
from django.contrib.auth.decorators import permission_required

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

@permission_required("is_superuser")
def List(request):
    _get = request.GET
    if ("search" in _get):
        products = models.Product.objects.filter(nombre__contains=_get["search"])
    else:
        products = models.Product.objects
    products = products.order_by("views")[::-1]
    context = {   
        "products": products,
    }
    return render(request, "products/List.html", context)

def Edit(request, _product_id):
    product = models.Product.objects.get(product_id = _product_id)
    data = {"category_id": product.category_id, "nombre": product.nombre}
    form = forms.Product(initial=data)
    context = {
        "product": product,
        "form": form
    }
    return render(request, "products/EditProduct.html", context)