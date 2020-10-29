from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import UsernameField, AuthenticationForm


class Custom_AuthenticationForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': True})
        )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'current-password'}),
    )