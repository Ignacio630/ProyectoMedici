from django.urls import path
from Proveedores.views import create_providers, list_providers

urlpatterns = [
    path('create_providers/',create_providers),
    path('list_providers/',list_providers),
]
