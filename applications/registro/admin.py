from django.contrib import admin
from .models import (
    Pais, Causa, SistemaServicio, AreaACargo, EmpresaMonitoreo, Agrupacion, Plataforma, Alcance,
    ClasificacionImpacto, TipoSolucion, ViaConocimiento, UsuariosAfectados, TipoSistema,
    Estado, Sistema, Participante, Servidor, Enlace, Region, Comuna, Ubicacion, Reporte,
    AccionPreventiva, MotivoIncidente, AccionIncidente, Seguimiento
    )

# Register your models here.
admin.site.register(Pais)
admin.site.register(Causa)
admin.site.register(SistemaServicio)
admin.site.register(AreaACargo)
admin.site.register(EmpresaMonitoreo)
admin.site.register(Agrupacion)
admin.site.register(Plataforma)
admin.site.register(Alcance)
admin.site.register(ClasificacionImpacto)
admin.site.register(TipoSolucion)
admin.site.register(ViaConocimiento)
admin.site.register(UsuariosAfectados)
admin.site.register(TipoSistema)
admin.site.register(Estado)
admin.site.register(Sistema)
admin.site.register(Participante)
admin.site.register(Servidor)
admin.site.register(Enlace)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Ubicacion)
admin.site.register(AccionPreventiva)
admin.site.register(MotivoIncidente)
admin.site.register(AccionIncidente)
admin.site.register(Seguimiento)

class ReporteAdmin(admin.ModelAdmin):
    list_display = (
        'detalle',
        'resumen',
        'impacto',
        'fecha_conocimiento',
        'indisponibilidad',
        'tiempo_indisponibilidad',
        'monitoreo',
        'fecha_incidente',
        'fecha_restauracion',
        'ciberseguridad',
        'causa_principal',
        'solucion',
        'analisis_posterior',
        'control_de_cambios',
        'ticket_OTRS',
        'duracion'
    )

    def duracion(self, obj):

        return obj.fecha_restauracion - obj.incidente

    search_fields =('detalle','fecha_incidente','control_de_cambios')

admin.site.register(Reporte, ReporteAdmin)

#Esto es para hacer prueba relacion bdd muchos a muchos

#class EstudianteAdmin(admin.ModelAdmin):
#    list_display = (
#        'name',
#        'lastname'
#    )

#admin.site.register(Estudiante, EstudianteAdmin)
#admin.site.register(Materia)