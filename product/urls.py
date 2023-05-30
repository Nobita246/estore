from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('details/<slug>', views.product_detail_page)
]
