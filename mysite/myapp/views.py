from django.shortcuts import render, redirect
from .models import Motos
# Create your views here.
def home(request):
    list_motos = Motos.objects.all()
    return render(request, "index.html", {"list_motos": list_motos})

def registrarMoto(request):
    modelo = request.POST['txtModelo']
    marca = request.POST['txtMarca']
    precio = request.POST['txtPrecio']

    moto = Motos.objects.create(modelo=modelo, marca=marca, precio=precio)
    return redirect('/')

def edicionMoto(request, moto_id):
    moto = Motos.objects.get(id=moto_id)
    return render(request, "edicionMoto.html", {"moto": moto})

def editMoto(request, moto_id):
    modelo = request.POST['txtModelo']
    marca = request.POST['txtMarca']
    precio = request.POST['txtPrecio']

    moto = Motos.objects.get(id=moto_id)
    moto.modelo = modelo
    moto.marca = marca
    moto.precio = precio
    moto.save()
    return redirect('/')


def eliminarMoto(request, moto_id):
    moto = Motos.objects.get(id=moto_id)
    moto.delete()
    return redirect('/')

