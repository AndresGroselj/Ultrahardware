from django.shortcuts import render

# Create your views here.


def Contact(request):
    context = {
    }
    return render(request, "contact/Contact.html", context)