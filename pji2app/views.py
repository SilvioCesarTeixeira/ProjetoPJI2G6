from django.shortcuts import render, redirect
from pji2app.forms import CadastroForm
from pji2app.models import Cadastro
from django.core.paginator import Paginator


def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Cadastro.objects.filter(inputCity__icontains=search)
    else:
        qry_data = Cadastro.objects.get_queryset().order_by(
            'id')  # Garante que o DB fornece um registro de cada vez, ordenado por Id
        paginator = Paginator(qry_data, 4)  # Exibe 4 registros do DB por página
        pages = request.GET.get('page')  # Captura qual é a página (page) selecionada no index.html pelo usuário
        data['db'] = paginator.get_page(pages)
    #   data['db'] = Cadastro.objects.all() ## Para buscar todos os registros do DB ## Linha para request sem paginação
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = CadastroForm()
    return render(request, 'form.html', data)


def create(request):
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Cadastro.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Cadastro.objects.get(pk=pk)
    data['form'] = CadastroForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Cadastro.objects.get(pk=pk)
    form = CadastroForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Cadastro.objects.get(pk=pk)
    db.delete()
    return redirect('home')
