from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registrarUsuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

def registrarProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarProductos')
    else:
        form = ProductoForm()
    return render(request, 'registrarProducto.html', {'form': form})

def listarProductos(request):
    productos = Producto.objects.all()
    return render(request, 'listarProductos.html', {'productos': productos})

def verCarrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    return render(request, 'verCarrito.html', {'carrito': carrito})

def cerrarSesion(request):
    logout(request)
    return redirect('index')

def iniciarSesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
            else: 
                return HttpResponse("Credenciales inválidas")
        else:
            return HttpResponse("Formulario inválido")
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})


            