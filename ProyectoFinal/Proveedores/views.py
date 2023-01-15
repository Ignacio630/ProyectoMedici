from django.shortcuts import render
from django.contrib import messages
from Proveedores.models import Providers
from Proveedores.forms import ProvidersForm

# Create your views here.

def create_providers(request):
    if request.method == 'GET':
        context = { 'form': ProvidersForm() }
        return render(request, 'Proveedores/create_providers.html', context=context)
    elif request.method == 'POST':
        form = ProvidersForm(request.POST)
        if form.is_valid():
            Providers.objects.create(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                phone = form.cleaned_data['phone'],
                address = form.cleaned_data['address']
            )
            context = {
                'form': form,
                'message.success': 'Proveedor creado correctamente'
            }

            return render(request, 'Proveedores/create_providers.html', context=context)
        else:
            context = {
                'form': form,
                'message': 'Error al crear el proveedor'
            }
            return render(request, 'Proveedores/create_providers.html', context=context)
    
    return render(request, 'Proveedores/create_providers.html', context={})

def list_providers(request):
    if 'search' in request.GET:
        search = request.GET['search']
        providers = Providers.objects.filter(name__icontains=search)
        providers = providers.order_by('name')
    else:
        providers = Providers.objects.all().order_by('name')
    context = {
        'providers': providers,
    }
    return render(request, 'Proveedores/list_providers.html', context=context)