from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'registro'

def Prueba(self):
    print('Hola mundo desde la app de registro de incidentes')

urlpatterns = [
    #path('registro/', PruebaView.as_view()),
    #path('registro/list', PruebaListView.as_view()),
    #path('registro/listado', RegistroListView.as_view()),
    #path('registro/create', RegistroCreateView.as_view()),

    # urls Pais
    path('listar_paises/', PaisListView.as_view(), name='listar_paises'),
    path('crea_pais/', PaisCreateView.as_view(), name='crea_pais'),
    path('listar_ubicaciones/', ListByComunaUbicaciones.as_view(), name='listar_ubicaciones'),
    path('listar_ubicaciones/<id>/', ListByComunaUbicacionesParametro.as_view(), name='listar_unicaciones_detalle'),
    path('listar_ubicaciones2/', ListByComunaUbicacionesParametro2.as_view(), name='listar_ubicaciones2'),
    path('detalle_comuna/<pk>/', ComunaDetailView.as_view(), name='detalle_comuna'),
    path('crea_comuna/', ComunaCreateView.as_view(), name='crea_comuna'),
    path('listar_comunas/', ListAllComunas.as_view(), name='listar_comunas'),
    path('editar_comuna/<int:pk>', ComunaUpdateView.as_view(), name='edita_comuna'),
    path('eliminar_comuna/<int:pk>', ComunaDeleteView.as_view(), name='elimina_comuna'),
    path('crea_region/', RegionCreateView.as_view(), name='crea_region'),
    path('listar_regiones/', RegionListView.as_view(), name='listar_regiones'),
    path('editar_region/<int:pk>', RegionUpdateView.as_view(), name='edita_region'),
    path('eliminar_region/<int:pk>', RegionDeleteView.as_view(), name='elimina_region'),
    path('inscribir_reporte/', ReporteCreateView.as_view(), name='crea_reporte'),
    path('listar_reportes/', ReporteListView.as_view(), name='listar_reportes'),
    path('crea_causa/', CausaCreateView.as_view(), name='crea_causa'),
    path('crea_sistema_servicio/', SistemaServicioCreateView.as_view(), name='crea_sistema_servicio'),
    path('crea_area_a_cargo/', AreaACargoCreateView.as_view(), name='crea_area_a_cargo'),
    path('crea_agrupacion/', AgrupacionCreateView.as_view(), name='crea_agrupacion'),
    path('crea_plataforma/', PlataformaCreateView.as_view(), name='crea_plataforma'),
]