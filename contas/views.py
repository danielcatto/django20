from django.shortcuts import render, redirect
from datetime import datetime
from .models import Transacao
from .form import TransacaoForm




# Create your views here.
def home(request):
    hora = datetime.now()
    dados = {}
    dados['now'] = hora
    return render(request, 'contas/home.html', dados)

def contato(request):
    return render(request, 'contas/contato.html')

def cadastro_usuarios(request):
    return render(request, 'contas/cadastro_usuarios.html')


def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    return render(request, 'contas/form.html', data)