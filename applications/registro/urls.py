from django.contrib import admin
from django.urls import path
from .views import *

def Prueba(self):
    print('Hola mundo desde la app de registro de incidentes')

urlpatterns = [
    #path('registro/', PruebaView.as_view()),
    #path('registro/list', PruebaListView.as_view()),
    #path('registro/listado', RegistroListView.as_view()),
    #path('registro/create', RegistroCreateView.as_view()),
]