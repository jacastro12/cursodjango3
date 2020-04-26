from django.shortcuts import render

# Create your views here.
from .models import *

def inicio (request):
    categorias = Categorias.objects.all()
    noticias = Noticias.objects.all()
    ctx= {"categorias":categorias, "noticias": noticias}
    return render(request, 'index.html', ctx)


def noticia_individual(request, pk):
    noticia = Noticias.objects.get(pk = pk)
    ctx={"noticia": noticia}
    return render(request, 'noticia_individual.html', ctx)
