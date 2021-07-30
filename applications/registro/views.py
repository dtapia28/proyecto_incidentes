from django.http import request
from django.http.response import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import *


# Create your views here.
#class 
# Esto es un ejemplo
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)





class ListByComunaUbicaciones(ListView):
    
    template_name = 'registro/ubicaciones.html'

    def get_queryset(self):
        lista = Ubicacion.objects.filter(
            comuna__nombre='El Bosque'
        )
        return lista


class ListByComunaUbicacionesParametro(ListView):

    template_name = 'registro/ubicaciones.html'

    def get_queryset(self):

        id = self.kwargs['id']
        lista = Ubicacion.objects.filter(
            comuna=id
        )
        return lista 


class ListByComunaUbicacionesParametro2(ListView):

    template_name = 'registro/ubicaciones2.html'

    def get_queryset(self):

        id = self.request.GET.get('id', '1')
        lista = Ubicacion.objects.filter(
            comuna=id
        )

        print("El id es "+str(id))
        return lista



class PaisListView(ListView):
    model = Pais
    template_name = "pais/list.html"

    def get_context_data(self, **kwargs):
        context = super(PaisCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Listado paises'
        context['url_create'] = reverse_lazy('registro:crea_pais')


class PaisCreateView(CreateView):
    model = Pais
    template_name = "pais/create.html"
    form_class =PaisForm

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == "add":
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = "No ha ingresado a ninguna opción"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super(PaisCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Registro nuevo país'
        context['url_create'] = reverse_lazy('registro:crea_pais')
        context['url_list'] = reverse_lazy('registro:crea_reporte')
        context['action'] = 'add'
        return context


class ComunaDetailView(DetailView):
    model = Comuna
    template_name = "registro/detalle_comuna.html"


class ComunaCreateView(CreateView):
    model = Comuna
    template_name = "comuna/create.html"
    form_class = ComunaForm
    success_url = reverse_lazy('registro:listar_comunas')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == "add":
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = "No ha ingresado a ninguna opción"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super(ComunaCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Registro nueva comuna'
        context['url_create'] = reverse_lazy('registro:crea_comuna')
        context['url_list'] = reverse_lazy('registro:listar_comunas')
        context['action'] = 'add'
        return context


class ComunaUpdateView(UpdateView):
    model = Comuna
    template_name = "comuna/edit.html"
    form_class = FormComuna
    success_url = reverse_lazy('registro:listar_comunas')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == "edit":
                form = self.get_form()
                data = form.save()
                print(data)
            else:
                data['error'] = "No ha ingresado a ninguna opción"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super(ComunaUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Editar comuna'
        context['url_list'] = reverse_lazy('registro:listar_comunas')
        context['action'] = 'edit'
        return context 


class ListAllComunas(ListView):

    template_name='registro/all_comunas.html'
    ordering='nombre'
    model=Comuna

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == "search_region_id":
                data = []
                for item in Region.objects.filter(pais_id=request.POST['id']):
                    data.append({'id':item.id, 'nombre':item.nombre})
            else:
                data['error'] = "No ha ingresado a ninguna opción"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context = super(ListAllComunas, self).get_context_data(**kwargs)
        context['regiones'] = Region.objects.all()
        context['paises'] = Pais.objects.all()
        context['url_create'] = reverse_lazy('registro:crea_comuna')
        context['form'] = ComunaForm()
        context['action'] = 'add'
        return context


class ComunaDeleteView(DeleteView):
    model = Comuna
    template_name = "comuna/delete.html"
    success_url = reverse_lazy('registro:listar_comunas')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)    

    def get_context_data(self, **kwargs):
        context = super(ComunaDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Eliminar '
        context['url_list'] = reverse_lazy('registro:listar_comunas')
        context['action'] = 'delete'
        return context    



class RegionCreateView(CreateView):
    model = Region
    template_name = "region/add.html"
    form_class = RegionForm
    success_url = reverse_lazy('registro:listar_regiones')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == "add":
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = "No ha ingresado a ninguna opción"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super(RegionCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Registro nueva región'
        context['url_create'] = reverse_lazy('registro:crea_region')
        context['url_list'] = reverse_lazy('registro:listar_regiones')
        context['action'] = 'add'        
        return context


class RegionListView(ListView):
    model = Region
    template_name = "region/list.html"

    def get_context_data(self, **kwargs):
        context = super(RegionListView, self).get_context_data(**kwargs)
        context['title'] = 'Listado regiones'
        context['url_create'] = reverse_lazy('registro:crea_region')
        context['url_list'] = reverse_lazy('registro:listar_regiones')
        context['url_edit'] = reverse_lazy('registro:edita_region')
        return context


class RegionUpdateView(UpdateView):
    model = Region
    template_name = "region/edit.html"
    form_class = RegionForm
    success_url = reverse_lazy('registro:listar_regiones')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == "edit":
                form = self.get_form()
                data = form.save()
                print(data)
            else:
                data['error'] = "No ha ingresado a ninguna opción"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super(RegionUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Editar región'
        context['url_list'] = reverse_lazy('registro:listar_regiones')
        context['action'] = 'edit'
        return context


class RegionDeleteView(DeleteView):
    model = Region
    template_name = "region/delete.html"
    success_url = reverse_lazy('registro:listar_regiones')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)    

    def get_context_data(self, **kwargs):
        context = super(RegionDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Eliminar '
        context['url_list'] = reverse_lazy('registro:listar_regiones')
        context['action'] = 'delete'
        return context



class ReporteCreateView(CreateView):

    model = Reporte
    template_name = "reporte/create.html"
    form_class = ReporteForm
    success_url = reverse_lazy('registro:listar_regiones')

    def post(self, request, *args, **kwargs):

        data = {}
        try:
            action = request.POST['action']
            if action == "add":
                form = self.get_form()
                data = form.save()
            elif action == "search_pais":
                data = []
                for item in Pais.objects.all():
                    data.append({'id':item.id, 'nombre':item.nombre})
            elif action == "search_causa":
                data = []
                for item in Causa.objects.all():
                    data.append({'id':item.id, 'nombre':item.nombre})
            elif action == 'search_sistema_servicio':
                data = []
                for item in SistemaServicio.objects.all():
                    data.append({'id':item.id, 'nombre':item.nombre})
            elif action == 'search_area_a_cargo':
                data = []
                for item in AreaACargo.objects.all():
                    data.append({'id':item.id, 'nombre':item.nombre})
            elif action == 'search_agrupacion':
                data = []
                for item in Agrupacion.objects.all():
                    data.append({'id':item.id, 'nombre':item.nombre})
            elif action == 'search_plataforma':
                data = []
                for item in Plataforma.objects.all():
                    data.append({'id':item.id, 'nombre':item.nombre})                                        
            else:
                data['error'] = "No ha ingresado a ninguna opción"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):

        context = super(ReporteCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Registro nuevo incidente'
        context['url_create'] = reverse_lazy('registro:crea_region')
        context['url_list'] = reverse_lazy('registro:listar_reportes')
        context['action'] = 'add'
        context['pais_form'] = PaisForm
        context['causa_form'] = CausaForm
        context['sistema_servicio_form'] = SistemaServicioForm
        context['area_a_cargo_form'] = AreaACargoForm
        context['agrupacion_form'] = AgrupacionForm
        context['plataforma_form'] = PlataformaForm
        return context



class ReporteListView(ListView):
    model = Reporte
    template_name = "reporte/list.html"

    def get_context_data(self, **kwargs):
        context = super(ReporteListView, self).get_context_data(**kwargs)
        context['title'] = 'Listado reportes'
        context['url_create'] = reverse_lazy('registro:crea_region')
        context['url_list'] = reverse_lazy('registro:listar_regiones')
        context['url_edit'] = reverse_lazy('registro:edita_region')
        return context


class CausaCreateView(CreateView):
    model = Causa
    template_name = "causa/create.html"
    form_class = CausaForm

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == "add":
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = "No ha ingresado a ninguna opción"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super(CausaCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Registro nueva causa'
        context['url_create'] = reverse_lazy('registro:crea_causa')
        context['url_list'] = reverse_lazy('registro:crea_reporte')
        context['action'] = 'add'
        return context



class SistemaServicioCreateView(CreateView):
    model = SistemaServicio
    template_name = "sistema_servicio/create.html"
    form_class = SistemaServicioForm

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == "add":
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = "No ha ingresado a ninguna opción"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super(SistemaServicioCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Registro nuevo sistema de servicios'
        context['url_create'] = reverse_lazy('registro:crea_sistema_servicio')
        context['url_list'] = reverse_lazy('registro:crea_reporte')
        context['action'] = 'add'
        return context


class AreaACargoCreateView(CreateView):
    model = AreaACargo
    template_name = "area_a_cargo/create.html"
    form_class = AreaACargoForm

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == "add":
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = "No ha ingresado a ninguna opción"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super(AreaACargoCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Registro nueva area a cargo'
        context['url_create'] = reverse_lazy('registro:crea_area_a_cargo')
        context['url_list'] = reverse_lazy('registro:crea_reporte')
        context['action'] = 'add'
        return context



class AgrupacionCreateView(CreateView):
    model = Agrupacion
    template_name = "agrupacion/create.html"
    form_class = AgrupacionForm

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == "add":
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = "No ha ingresado a ninguna opción"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super(AreaACargoCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Registro nueva agrupación'
        context['url_create'] = reverse_lazy('registro:crea_agrupacion')
        context['url_list'] = reverse_lazy('registro:crea_reporte')
        context['action'] = 'add'
        return context



class PlataformaCreateView(CreateView):
    model = Plataforma
    template_name = "plataforma/create.html"
    form_class = PlataformaForm

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == "add":
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = "No ha ingresado a ninguna opción"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super(PlataformaCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Registro nueva plataforma'
        context['url_create'] = reverse_lazy('registro:crea_plataforma')
        context['url_list'] = reverse_lazy('registro:crea_reporte')
        context['action'] = 'add'
        return context
