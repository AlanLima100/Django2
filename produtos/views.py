from django.shortcuts import render
# funções que serão chamadas por nossas rotas pra então abrir os templetes para visualização
from .models import Produto1

def index(request):
    produtos = Produto1.objects.all()


    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa',
        'produtos': produtos
    }
    return render (request, 'index.html', context)

def contato(resquest):
    return render( resquest, 'contato.html')

def produto(request, id):
    prod = Produto1.objects.get(id=id)
    
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)
