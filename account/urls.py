from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.login),
    path("register/", views.register),
    path("activate/user/<email_token>/", views.activate_user),
]
