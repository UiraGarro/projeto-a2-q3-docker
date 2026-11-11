from django.shortcuts import render, redirect
from .models import Registro

def index(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        mensagem = request.POST.get('mensagem')
        Registro.objects.create(nome=nome, mensagem=mensagem)
        return redirect('index')

    registros = Registro.objects.all().order_by('-criado_em')
    return render(request, 'cadastro/index.html', {'registros': registros})