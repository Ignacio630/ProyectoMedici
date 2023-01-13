from django.shortcuts import render

# Create your views here.

def create_product(request):
    return render(request, 'create_product.html', context={})


def list_product(request):
    return render(request, 'list_product.html', context={})