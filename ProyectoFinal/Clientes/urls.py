from django.urls import path
from .views import create_client

urlpatterns = [
    path('create_clients/',create_client),
]