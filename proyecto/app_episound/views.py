
from django.shortcuts import render
from django.http import HttpResponse
from .in_memory_data import canciones
# Create your views here.

def index(request):
  return render(request, "inicio/page.html") 

def miMusica(request):
  return render(request, "miMusica/page.html")

def buscar(request):
  return render(request, "buscador/page.html")

def mostrar_cancion(request):
    context = {
        'canciones': canciones
    }
    return render(request, "inicio/page.html", context)

def reproducir(request):
  return render(request, "reproduccion/page.html")

def inicio(request):
  return render(request, "inicio.html")