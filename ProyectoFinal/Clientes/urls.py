from django.urls import path
from .views import create_client, list_clients

urlpatterns = [
    path('create_clients/',create_client),
    path('list_clients/',list_clients),
]