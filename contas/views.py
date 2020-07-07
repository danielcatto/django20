from django.shortcuts import render
from datetime import datetime
from .models import Transacao





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

