from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, logout
# Create your views here.

def Login(request):
    if request.method == "POST":
        form = forms.Custom_AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("home")
    else:
        form = forms.Custom_AuthenticationForm()
        context = {
            "form": form
        }
        return render(request, "accounts/Login.html", context)

def Logout(request):
    logout(request)
    return redirect("home")