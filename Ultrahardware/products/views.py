from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib.auth.decorators import permission_required

# Create your views here.

def Product(request, _product_id):
    category_parents = models.Category_parent.objects.order_by("order")
    product = models.Product.objects.get(product_id = _product_id)
    context = {
        "category_parents": category_parents,
        "product": product
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

@permission_required("is_superuser")
def Edit(request, _product_id):
    if (request.method == "GET"):
        product = models.Product.objects.get(product_id = _product_id)
        data = {
            "product_id": product.product_id, 
            "category_id": product.category_id, 
            "nombre": product.nombre,
            "imagen_principal": product.imagen_principal,
            "precio": product.precio,
            "stock": product.stock,
            "description": product.description,
            "specs": product.specs,
            "views": product.views,
            "garantia": product.garantia,
            }
        form = forms.Product(initial=data)
        context = {
            "product": product,
            "form": form
        }
        return render(request, "products/EditProduct.html", context)
    elif (request.method == "POST"):
        _instance = models.Product.objects.get(product_id = _product_id)
        _form = forms.Product(request.POST, request.FILES)
        
        if (request.POST['action'] == "Update"):
            if (_form.is_valid()):
                if (_form.cleaned_data['imagen_principal']):
                    _instance.imagen_principal = _form.cleaned_data["imagen_principal"]
                _instance.category_id = _form.cleaned_data["category_id"]
                _instance.nombre = _form.cleaned_data["nombre"]
                _instance.precio = _form.cleaned_data["precio"]
                _instance.stock = _form.cleaned_data["stock"]
                _instance.description = _form.cleaned_data["description"]
                _instance.specs = _form.cleaned_data["specs"]
                _instance.garantia = _form.cleaned_data["garantia"]
                _instance.save()
        elif (request.POST['action'] == "Delete"):
            _instance.delete()
            
        return redirect("products:list")

@permission_required("is_superuser")
def Add(request):
    if (request.method == "GET"):
        data = {
            "product_id": 0, 
            "views": 0,
            }
        _form = forms.Product(initial=data)

    elif (request.method == "POST"):
        _instance = models.Product()
        _form = forms.Product(request.POST, request.FILES)
        
        if (_form.is_valid()):
            if (_form.cleaned_data['imagen_principal']):
                _instance.imagen_principal = _form.cleaned_data["imagen_principal"]
            _instance.category_id = _form.cleaned_data["category_id"]
            _instance.nombre = _form.cleaned_data["nombre"]
            _instance.precio = _form.cleaned_data["precio"]
            _instance.stock = _form.cleaned_data["stock"]
            _instance.description = _form.cleaned_data["description"]
            _instance.specs = _form.cleaned_data["specs"]
            _instance.garantia = _form.cleaned_data["garantia"]
            _instance.save()
            
            return redirect("products:list")
    context = {
            "form": _form
        }
    return render(request, "products/AddProduct.html", context)
            