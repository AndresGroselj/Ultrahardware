from django import forms
from . import models
from django.utils.translation import gettext, gettext_lazy as _


class Product(forms.ModelForm):
    category_id = forms.ModelChoiceField(
        label=_("category"),
        queryset=models.Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    nombre = forms.CharField(
        label=_("nombre"),
        strip=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    imagen_principal = forms.ImageField(
        label=_("Imagen principal"),
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    precio = forms.IntegerField(
        label=_("Precio"),
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '1'})
    )
    stock = forms.IntegerField(
        label=_("Stock"),
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0'})
    )
    description = forms.CharField(
        label=_("Descipcion"),
        strip=False,
        widget=forms.Textarea(attrs={'class': 'form-control'}),
    )
    specs = forms.CharField(
        label=_("Especificaciones"),
        strip=False,
        widget=forms.Textarea(attrs={'class': 'form-control'}),
    )
    class Meta:
        model = models.Product
        fields = ()