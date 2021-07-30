from django import forms
from django.forms import fields, models, widgets
from django.forms.forms import Form
from .models import *
import datetime


class FormComuna(forms.ModelForm):

    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ingresa el nombre de la comuna',
                'autocomplete': 'off',
                'autofocus': True
            }
        )
    )

    region = forms.ModelChoiceField(
        queryset = Region.objects.filter(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Escoge una región'
    )

    class Meta:
        model = Comuna
        fields = ['nombre', 'region']


    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors    
        except Exception as e:
            data['error'] = str(e)
        return data   

class RegionForm(forms.ModelForm):

    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ingresa el nombre de la región',
                'autocomplete': 'off',
                'autofocus': True
            }
        )
    )

    pais = forms.ModelChoiceField(
        queryset = Pais.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Escoge un país'
    )

    class Meta:
        model = Region    
        fields = ['nombre', 'pais']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors    
        except Exception as e:
            data['error'] = str(e)
        return data

class ComunaForm(forms.ModelForm):

    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ingresa el nombre de la comuna',
                'autocomplete': 'off',
                'autofocus': True
            }
        )
    )

    pais = forms.ModelChoiceField(
        queryset = Pais.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Escoge un país'
    )

    region = forms.ModelChoiceField(
        queryset = Region.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Escoge una región'
    )

    class Meta:
        model = Comuna
        fields = ['nombre', 'region']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors    
        except Exception as e:
            data['error'] = str(e)
        return data

class ReporteForm(forms.ModelForm):

    detalle = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder': 'Ingresa detalle del reporte',
                'autocomplete': 'off',
                'autofocus': True
            }
        )
    )

    resumen = forms.CharField(
        max_length=100,
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder': 'Ingresa resumen del reporte',
                'autocomplete': 'off'
            }
        )
    )    

    impacto = forms.CharField(
        max_length=100,
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder': 'Ingresa resumen del reporte',
                'autocomplete': 'off'
            }
        )
    )

    fecha_conocimiento = forms.DateTimeField(
        initial=datetime.datetime.today,
        widget=forms.DateTimeInput(
            attrs= {
                'class':'form-control',
                'autocomplete': 'off'
            }
        )
    )

    indisponibilidad = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    tiempo_indisponibilidad = forms.DateTimeField(
        initial=datetime.datetime.now,
        widget=forms.DateTimeInput(
            attrs= {
                'class':'form-control',
                'autocomplete': 'off'
            }
        )
    )

    monitoreo = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    fecha_incidente = forms.DateTimeField(
        initial=datetime.datetime.today,
        widget=forms.DateTimeInput(
            attrs= {
                'class':'form-control',
                'autocomplete': 'off'
            }
        )
    )

    fecha_restauracion = forms.DateTimeField(
        label="Fecha restauración",
        initial=datetime.datetime.today,
        widget=forms.DateTimeInput(
            attrs= {
                'class':'form-control',
                'autocomplete': 'off'
            }
        )
    )

    ciberseguridad = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    causa_principal = forms.CharField(
        max_length=100,
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Ingresa la causa principal de incidente',
                'autocomplete': 'off',
            }
        )
    )

    solucion = forms.CharField(
        max_length=300,
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Ingresa la solución del incidente',
                'autocomplete': 'off',
            }
        )
    )

    analisis_posterior = forms.CharField(
        label = "Análisis posterior",
        max_length=100,
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Ingresa el análisis posterior del incidente',
                'autocomplete': 'off',
            }
        )
    )

    control_de_cambios = forms.CharField(
        max_length=200,
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'control de cambios',
                'autocomplete': 'off',
            }
        )
    )

    ticket_OTRS = forms.CharField(
        max_length=200,
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Ticket OTRS',
                'autocomplete': 'off',
            }
        )
    )

    pais = forms.ModelChoiceField(
        queryset = Pais.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Escoge un país'
    )

    causa = forms.ModelChoiceField(
        queryset= Causa.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Escoge una causa'
    )

    sistema_servicio = forms.ModelChoiceField(
        queryset= SistemaServicio.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Escoge un sistema de servicio'
    )

    area_a_cargo = forms.ModelChoiceField(
        queryset=AreaACargo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Escoge un area a cargo'
    )

    agrupacion = forms.ModelChoiceField(
        label="Agrupación",
        queryset=Agrupacion.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Escoge una agrupación'
    )

    plataforma = forms.ModelChoiceField(
        queryset=Plataforma.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Escoge una plataforma'
    )

    alcance = forms.ModelChoiceField(
        queryset=Alcance.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Escoge un alcance'
    )

    clasificacion_impacto = forms.ModelChoiceField(
        label="Clasificación de impacto",
        queryset=ClasificacionImpacto.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Escoge clasificación de impacto'
    )

    tipo_solucion = forms.ModelChoiceField(
        label="Tipo de solución",
        queryset=TipoSolucion.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Escoge el tipo de solución'
    )

    via_conocimiento = forms.ModelChoiceField(
        queryset=ViaConocimiento.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Escoge una vía de conocimiento'
    )

    usuarios_afectados = forms.ModelChoiceField(
        queryset=UsuariosAfectados.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Escoge usuarios afectados'
    )

    tipo_sistema = forms.ModelChoiceField(
        queryset=TipoSistema.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Escoge tipo de sistema'
    )

    estado = forms.ModelChoiceField(
        queryset=Estado.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Escoge un estado'
    )

    empresas_monitoreo = forms.ModelMultipleChoiceField(
        queryset=EmpresaMonitoreo.objects.all(),
        widget= forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    sistemas = forms.ModelMultipleChoiceField(
        queryset=Sistema.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    participantes = forms.ModelMultipleChoiceField(
        queryset=Participante.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    servidor = forms.ModelMultipleChoiceField(
        label = "Servidores",
        queryset=Servidor.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    enlace = forms.ModelMultipleChoiceField(
        label = "Enlaces",
        queryset=Enlace.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    ubicacion = forms.ModelMultipleChoiceField(
        label = "Ubicaciones",
        queryset=Ubicacion.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )


    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors    
        except Exception as e:
            data['error'] = str(e)
        return data

    class Meta:
        model = Reporte
        fields = '__all__'


class PaisForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ingresa el nombre del país',
                'autocomplete': 'off',
                'autofocus': True
            }
        )
    )

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors    
        except Exception as e:
            data['error'] = str(e)
        return data

    class Meta:
        model = Pais
        fields = '__all__'


class CausaForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ingresa causa',
                'autocomplete': 'off',
                'autofocus': True
            }
        )
    )

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors    
        except Exception as e:
            data['error'] = str(e)
        return data

    class Meta:
        model = Causa
        fields = '__all__'

class SistemaServicioForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ingresa sistema de servicios',
                'autocomplete': 'off',
                'autofocus': True
            }
        )
    )

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors    
        except Exception as e:
            data['error'] = str(e)
        return data

    class Meta:
        model = SistemaServicio
        fields = '__all__'


class AreaACargoForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ingresa área a cargo',
                'autocomplete': 'off',
                'autofocus': True
            }
        )
    )

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors    
        except Exception as e:
            data['error'] = str(e)
        return data

    class Meta:
        model = AreaACargo
        fields = '__all__'


class AgrupacionForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ingresa agrupación',
                'autocomplete': 'off',
                'autofocus': True
            }
        )
    )

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors    
        except Exception as e:
            data['error'] = str(e)
        return data

    class Meta:
        model = Agrupacion
        fields = '__all__'


class PlataformaForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ingresa plataforma',
                'autocomplete': 'off',
                'autofocus': True
            }
        )
    )

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors    
        except Exception as e:
            data['error'] = str(e)
        return data

    class Meta:
        model = Plataforma
        fields = '__all__'