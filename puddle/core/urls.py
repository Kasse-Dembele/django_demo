from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import forms


app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/",views.contact, name="contact" ),
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(authentication_form=forms.LoginForm, template_name="core/login.html"), name="login")

    
]