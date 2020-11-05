from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import UsernameField, AuthenticationForm, UserCreationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
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
    email = forms.EmailField(
        label=_("Email"),
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control',}),
    )
    username = UsernameField(
        label=_("Nombre"),
        strip=False,
        widget=forms.TextInput(attrs={'class': 'form-control',}),
    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}),
        help_text=_("""  
            Su contraseña no puede ser muy similar a su nombre de usuario.<br>
            Su contraseña debe contener al menos 8 caracteres.<br>
            Su contraseña no puede ser muy comun.<br>
            Su contraseña no puede ser completamente numerica.<br><br>
            """),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Para verificar, introduzca la misma contraseña anterior.<br><br>"),
    )

    class Meta:
        model = User
        fields = ("email", "username",)

class Custom_PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'email'})
    )

class Custom_SetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("""  
            Su contraseña no puede ser muy similar a su nombre de usuario.<br>
            Su contraseña debe contener al menos 8 caracteres.<br>
            Su contraseña no puede ser muy comun.<br>
            Su contraseña no puede ser completamente numerica.<br><br>
            """),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}),
    )