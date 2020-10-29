from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("home")
    else:
        form = AuthenticationForm()
        context = {
            "form": form
        }
        return render(request, "accounts/Login.html", context)

def Logout(request):
    logout(request)
    return redirect("home")