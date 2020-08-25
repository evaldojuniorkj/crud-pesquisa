from django.shortcuts import render, redirect, get_object_or_404
from .forms import CarroForm
from .models import Carro

# Create your views here.

def cadastrar_carro(request, template_name='carro_form.html'):
    form = CarroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_carro')
    return render(request, template_name, {'form': form})

def listar_carro(request, template_name='carro_list.html'):
    query = request.GET.get("busca")
    if query:
        carros = Carro.objects.filter(modelo__icontains=query)
    else:
        carros = Carro.objects.all()
    return render(request, template_name, {'carros': carros})

def editar_carro(request,pk, template_name='carro_form.html'):
    carro = get_object_or_404(Carro, pk=pk)
    if request.method == "POST":
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('listar_carro')
    else:
        form = CarroForm(instance=carro)
    return render(request, template_name, {'form': form})

def remover_carro(request,pk, template_name='carro_delete.html'):
    carro = Carro.objects.get(pk = pk)
    if request.method == "POST":
        carro.delete()
        return redirect('listar_carro')
    return render(request, template_name, {'carro': carro})
