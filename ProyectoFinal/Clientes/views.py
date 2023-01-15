from django.shortcuts import render
from Clientes.models import Clients
from Clientes.forms import ClientsForm

def create_client(request):
    if request.method == 'GET':
        context = { 'form': ClientsForm() }
        return render(request, 'Clientes/create_clients.html', context=context)
    
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
            return render(request, 'Clientes/create_clients.html', context=context)
        else:
            context = {
                'form': form,
                'message': 'Error al crear el cliente'
            }
            return render(request, 'Clientes/create_clients.html', context=context)
        

def list_clients(request):
    if 'search' in request.GET:
        search = request.GET['search']
        clients = Clients.objects.filter(name__icontains=search)
        clients = clients.order_by('name')
    else:
        clients = Clients.objects.all().order_by('name')
    context = {
        'clients': clients
    }
    return render(request, 'Clientes/list_clients.html', context=context)