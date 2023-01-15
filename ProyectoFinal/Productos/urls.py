from django.urls import path
from Productos.views import create_products, list_products

urlpatterns = [
    path('create_products/',create_products),
    path('list_products/',list_products),
]