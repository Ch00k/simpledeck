from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import RedirectView, TemplateView
from django_registration import forms
from django_registration.backends.activation import views

app_name = "simpledeck"
handler404 = "simpledeck.views.handler404"

login = [
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
]

registration = [
    path(
        "accounts/activate/complete/",
        TemplateView.as_view(
            template_name="django_registration/activation_complete.html"
        ),
        name="django_registration_activation_complete",
    ),
    path(
        "accounts/activate/<str:activation_key>/",
        views.ActivationView.as_view(),
        name="django_registration_activate",
    ),
    path(
        "accounts/register/",
        views.RegistrationView.as_view(form_class=forms.RegistrationFormUniqueEmail),
        name="django_registration_register",
    ),
    path(
        "accounts/register/complete/",
        TemplateView.as_view(
            template_name="django_registration/registration_complete.html"
        ),
        name="django_registration_complete",
    ),
    path(
        "accounts/register/closed/",
        TemplateView.as_view(
            template_name="django_registration/registration_closed.html"
        ),
        name="django_registration_disallowed",
    ),
]

password_management = [
    path(
        "accounts/change-password/",
        auth_views.PasswordChangeView.as_view(
            template_name="change_password.html", success_url="/"
        ),
        name="change_password",
    ),
    path(
        "accounts/password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="password_reset.html",
            subject_template_name="password_reset_subject.txt",
            email_template_name="password_reset_email.html",
        ),
        name="password_reset",
    ),
    path(
        "accounts/password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "accounts/password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "accounts/password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]

urlpatterns = (
    login
    + registration
    + password_management
    + [
        path("", RedirectView.as_view(url="decks/")),
        path("decks/", include("deck.urls")),
    ]
)
