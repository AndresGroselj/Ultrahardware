from django.shortcuts import render

# Create your views here.


def Home(request):
    products = list(range(5))
    context = {   
        "products": products 
    }
    return render(request, "Home.html", context)