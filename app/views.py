from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa
from .forms import FormPessoa
#from django.contrib.messages import constants
from django.contrib import messages

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'home.html', {'pessoas': pessoas})


def cadastrar(request):
    if request.method == 'GET':
        form = FormPessoa()
        return render(request, 'forms.html', {'form': form})
    elif request.method == 'POST':
        form = FormPessoa(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('home')

def remover(request, id):
    try:
        pessoa = get_object_or_404(Pessoa, id=id)
        pessoa.delete()
        return redirect('home')
    except Exception as e:
        messages.error(request, 'Erro ao excluir esta pessoa!')
        return redirect('home')

def editar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)

    form = FormPessoa(request.POST or None, instance=pessoa)
    
    if request.method == 'GET':
        return render(request, 'forms.html', {'form':form})
    elif request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')