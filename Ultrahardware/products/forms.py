from django import forms
from . import models
from django.utils.translation import gettext, gettext_lazy as _

class Product(forms.Form):
    product_id = forms.IntegerField(
        label=_("id"),
        widget=forms.HiddenInput()
    )
    category_id = forms.ModelChoiceField(
        label=_("category"),
        required=True,
        queryset=models.Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}), 
    )
    nombre = forms.CharField(
        label=_("nombre"),
        strip=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    imagen_principal = forms.ImageField(
        label=_("Imagen principal"),
        required = False,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    precio = forms.IntegerField(
        label=_("Precio"),
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '2147483647'})
    )
    stock = forms.IntegerField(
        label=_("Stock"),
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '2147483647'})
    )
    description = forms.CharField(
        label=_("Descipcion"),
        strip=False,
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'}),
    )
    specs = forms.CharField(
        label=_("Especificaciones"),
        strip=False,
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'}),
    )
    views = forms.IntegerField(
        label=_("views"),
        widget=forms.HiddenInput()
    )
    class Meta:
        model = models.Product
        fields = ()