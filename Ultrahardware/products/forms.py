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
    class Meta:
        model = models.Product
        fields = ("category_id", "nombre", "imagen_principal")