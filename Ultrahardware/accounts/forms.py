from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import UsernameField, AuthenticationForm, UserCreationForm
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)


class Custom_AuthenticationForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': True})
        )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'current-password'}),
    )

class Custom_UserCreationForm(UserCreationForm):
    username = UsernameField(
        label=_("Nombre"),
        strip=False,
        widget=forms.TextInput(attrs={}),
    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )