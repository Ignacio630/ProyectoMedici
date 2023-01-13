from django.shortcuts import render
from Clientes.models import Clients
from Clientes.forms import ClientsForm
# Create your views here.

def create_client(request):
    if request.method == 'GET':
        form = ClientsForm()
        return render(request, 'create_client', context={'form': form})
    
    elif request.method == 'POST':
        form = ClientsForm(request.POST)
        if form.is_valid():
            Clients.objects.create(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                phone = form.cleaned_data['phone'],
                address = form.cleaned_data['address']
            )
            context = {
                'form': form,
                'message': 'Cliente creado correctamente'
            }
            return render(request, 'create_client', context=context)
        else:
            context = {
                'form': form,
                'message': 'Error al crear el cliente'
            }
            return render(request, 'create_client', context=context)