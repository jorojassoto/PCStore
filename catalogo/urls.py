from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrarComponente/', views.registrarComponente, name='registrarComponente'),
    path('listarProductos/', views.listarProductos, name='listarProductos'),
    path('registrar/', views.registrarUsuario, name='registrar'),
]