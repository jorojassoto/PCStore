from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registrarUsuario(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'registro.html', {'form': UserCreationForm, 'error': 'El nombre de usuario ya existe'})
        return render(request, 'registro.html', {'form': UserCreationForm, 'error': 'Las contraseñas no coinciden'})

def registrarComponente(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarProductos')
    else:
        form = ProductoForm()
    return render(request, 'catalogo/registrarProducto.html', {'form': form})

def listarProductos(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo/listarProductos.html', {'productos': productos})

def verCarrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    return render(request, 'catalogo/verCarrito.html', {'carrito': carrito})


            