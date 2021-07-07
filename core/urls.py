from django.urls import path
from .views import *

urlpatterns = [
    path('',VentanaPrincipal,name='VentanaPrincipal'),
    path('Noticias',Noticias,name='Noticias'),
    path('Sesion',Sesion,name='Sesion'),
    path('VarianteDelta',VarianteDelta,name='VarianteDelta'),
    path('Charquican',Charquican,name='Charquican'),
    path('bravovidal',bravovidal,name='bravovidal'),
    path('ingresar',ingresar,name='ingresar'),
    path('modificar/<id>',modificarusuario,name='modificar'),
    path('eliminar/<id>',eliminar,name='eliminar'),
    path('ver',ver,name='ver'),
]