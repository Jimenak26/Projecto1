from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader

from clientes.forms import ClienteFormulario
from clientes.models import Cliente


# Create your views here.
def agregar(request):
    pagina = loader.get_template('clientes/agregar.html')
    if request.method == 'GET':
        formulario = ClienteFormulario
    elif request.method == 'POST':
        formulario = ClienteFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))


def modificar(request, id):
    pagina = loader.get_template('clientes/modificar.html')
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == 'GET':
        formulario = ClienteFormulario(instance=cliente)
    elif request.method == 'POST':
        formulario = ClienteFormulario(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))


def ver(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    datos = {'clientes': cliente}
    pagina = loader.get_template('clientes/ver.html')
    return render(request, 'clientes/ver.html', {'cliente': cliente})


def eliminar(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if cliente:
        cliente.delete()
        return redirect('inicio')
