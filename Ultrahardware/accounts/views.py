from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, logout
# Create your views here.


def Signup(request):
    if request.method == "POST":
        form = forms.Custom_UserCreationForm(request.POST)
        if form.is_valid():
            print(" if form.iSAVING NEW USER")
            user = form.save()

            login(request, user)
            return redirect("home")
    else:
        form = forms.Custom_UserCreationForm()
    context = {
        "form" : form
    }
    return render(request, "accounts/Signup.html", context)

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

def Password_reset(request):
    if request.method == "POST":
        form = forms.Custom_PasswordResetForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:password_reset_done")
    else:
        form = forms.Custom_PasswordResetForm()
    context = {
        "form": form 
    }
    return render(request, "accounts/passwordReset/Password_reset.html", context)

def Password_reset_done(request):
    context = {
    }
    return render(request, "accounts/passwordReset/Password_reset_done.html", context)

def Reset(request, _uidb64, _token):
    context = {
    }
    return render(request, "accounts/passwordReset/Reset.html", context)

def Reset_done(request):
    context = {
    }
    return render(request, "accounts/passwordReset/Reset_done.html", context)

