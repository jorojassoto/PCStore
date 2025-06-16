from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('registrarProducto/', views.registrarProducto, name='registrarProducto'),
    path('listarProductos/', views.listarProductos, name='listarProductos'),
    path('registro/', views.registrarUsuario, name='registro'),
    path('login/', views.iniciarSesion, name='login'),
    path('logout/', views.cerrarSesion, name='logout'),
]