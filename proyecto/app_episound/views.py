from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  return render(request, "inicio/page.html") 

def miMusica(request):
  return render(request, "miMusica/page.html")

def buscar(request):
  return render(request, "buscador/page.html")

def reproducir(request):
  return render(request, "reproduccion/page.html")