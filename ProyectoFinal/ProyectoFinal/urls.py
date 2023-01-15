from django.contrib import admin
from django.urls import path
from ProyectoFinal.views import index
from Clientes.views import create_client, list_clients
from Proveedores.views import create_providers, list_providers
from Productos.views import create_products, list_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index/', index),
    path('create-clients/', create_client),
    path('create-providers/', create_providers),
    path('create-products/', create_products),
    path('list-clients/', list_clients),
    path('list-providers/', list_providers),
    path('list-products/', list_products),
]
