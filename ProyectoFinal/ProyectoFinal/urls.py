from django.contrib import admin
from django.urls import path
from ProyectoFinal.views import index
from Clientes.views import create_client
from Proveedores.views import create_provider
from Productos.views import create_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('create-clients', create_client),
    path('create-provider/', create_provider),
    path('create-product/', create_product),
]
