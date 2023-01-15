from django.shortcuts import render
from Productos.models import Product
from Productos.forms import ProductsForm
# Create your views here.

def create_products(request):
    if request.method == 'GET':
        context = { 'form': ProductsForm() }
        return render(request, 'Productos/create_products.html', context=context)
    elif request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            Product.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                stock = form.cleaned_data['stock'],
                category = form.cleaned_data['category'],
                description = form.cleaned_data['description']
            )
            context = {
                'form': form,
                'message': 'Producto creado correctamente'
            }
            return render(request, 'Productos/create_products.html', context=context)
        else:
            context = {
                'form': form,
                'message': 'Error al crear el producto'
            }
            return render(request, 'Productos/create_products.html', context=context)
            
    return render(request, 'Productos/create_products.html', context={})

def list_products(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products = Product.objects.filter(name__icontains=search)
        products = products.order_by('name')
    else:
        products = Product.objects.all().order_by('name')
    context = {
        'products': products
    }

    return render(request, 'Productos/list_products.html', context=context)