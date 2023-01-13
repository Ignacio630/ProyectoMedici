from django.shortcuts import render

# Create your views here.

def create_provider(request):
    return render(request, 'create_provider.html', context={})

def list_provider(request):
    return render(request, 'list_provider.html', context={})