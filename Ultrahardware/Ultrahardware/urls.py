"""Ultrahardware URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse
from contact import views as contact_views
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name="home"),
    path('location/', views.Location, name="location"),
    path('cart/', include("cart.urls")),
    path('product/', include("products.urls")),
    path('contact/', contact_views.Contact, name="contact"),
    path('accounts/', include("accounts.urls")),

    path('redirect/<_app>/<_name>', views.Redirect,),
    path('redirect/accounts/password_reset_done', views.Redirect, name="password_reset_done"),
    path('redirect/accounts/password_reset_complete', views.Redirect, name="password_reset_complete"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)