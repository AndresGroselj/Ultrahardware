from django.shortcuts import render

# Create your views here.

def Cart(request):
    context = {
    }
    return render(request, "cart/Cart.html", context)