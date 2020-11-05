from django.urls import path
from . import views
from .forms import Custom_PasswordResetForm, Custom_SetPasswordForm

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = "accounts"

urlpatterns = [
    path("signup/", views.Signup, name="signup"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),

    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/passwordReset/Password_reset.html",
            email_template_name="emails/password_reset_email.html",
            success_url=reverse_lazy("accounts:password_reset_done"),
            form_class=Custom_PasswordResetForm,
            ),
        name="reset_password"
    ),
    path(
        "password_reset/done/", 
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/passwordReset/Password_reset_done.html",
        ),
        name="password_reset_done"
    ),
    path(
        "reset/<uidb64>/<token>/", 
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy("accounts:password_reset_complete"),
            template_name="accounts/passwordReset/Reset.html",
            form_class=Custom_SetPasswordForm,
        ), 
        name="password_reset_confirm"
    ),
    path(
        "reset/done/", 
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/passwordReset/Reset_done.html",
        ), 
        name="password_reset_complete"
    ),
]