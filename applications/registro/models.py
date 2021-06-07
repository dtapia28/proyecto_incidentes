from django.db import models


# Create your models here.

class Pais(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    created = models.DateTimeField('creado', auto_now=False, auto_now_add=True)
    edited = models.DateTimeField('editado', auto_now=True, auto_now_add=False)


    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'


    def __str__(self):
        return self. nombre


class Causa(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    created = models.DateTimeField('creado', auto_now=False, auto_now_add=True)
    edited = models.DateTimeField('editado', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Causa'
        verbose_name_plural = 'Causas'

    def __str__(self):
        return self.nombre


class SistemaServicio(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    created = models.DateTimeField('creado', auto_now=False,auto_now_add=True)
    edited = models.DateTimeField('editado', auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Sistema de servicio'
        verbose_name_plural = 'Sistemas de servicios'

    def __str__(self):
        return self.nombre


class AreaACargo(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    created = models.DateTimeField('creado', auto_now=False,auto_now_add=True)
    edited = models.DateTimeField('editado', auto_now=True,auto_now_add=False) 

    
class EmpresaMonitoreo(models.Model):
    nombre = models.CharField('nombre',max_length=50)
    created = models.DateTimeField('creado', auto_now=False,auto_now_add=True)
    edited = models.DateTimeField('editado', auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Empresa monitoreo'
        verbose_name_plural = 'Empresas monitoreo'

    def __str__(self):
        return self.nombre


class Agrupacion(models.Model):
    nombre = models.CharField('nombre',max_length=50)
    created = models.DateTimeField('creado', auto_now=False,auto_now_add=True)
    edited = models.DateTimeField('editado', auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Agrupación'
        verbose_name_plural = 'Agrupaciones'

    def __str__(self):
        return self.nombre
        

class Plataforma(models.Model):
    nombre = models.CharField('nombre',max_length=50)
    created = models.DateTimeField('creado', auto_now=False,auto_now_add=True)
    edited = models.DateTimeField('editado', auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Plataforma'
        verbose_name_plural = 'Plataformas'

    def __str__(self):
        return self.nombre


class Alcance(models.Model):
    detalle = models.CharField('nombre',max_length=50)
    created = models.DateTimeField('creado', auto_now=False,auto_now_add=True)
    edited = models.DateTimeField('editado', auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Alcance'
        verbose_name_plural = 'Alcances'

    def __str__(self):
        return self.detalle


class ClasificacionImpacto(models.Model):
    detalle = models.CharField('nombre',max_length=50)
    created = models.DateTimeField('creado', auto_now=False,auto_now_add=True)
    edited = models.DateTimeField('editado', auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Clasificación de impacto'
        verbose_name_plural = 'Clasificaciones de impacto'

    def __str__(self):
        return self.detalle


class TipoSolucion(models.Model):
    detalle = models.CharField('nombre',max_length=50)
    created = models.DateTimeField('creado', auto_now=False,auto_now_add=True)
    edited = models.DateTimeField('editado', auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Tipo de solución'
        verbose_name_plural = 'Tipos de solución'

    def __str__(self):
        return self.detalle


class ViaConocimiento(models.Model):
    detalle = models.CharField('nombre',max_length=50)
    created = models.DateTimeField('creado', auto_now=False,auto_now_add=True)
    edited = models.DateTimeField('editado', auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Via de conocimiento'
        verbose_name_plural = 'Vias de conocimiento'

    def __str__(self):
        return self.detalle


class UsuariosAfectados(models.Model):
    detalle = models.CharField('nombre',max_length=50)
    created = models.DateTimeField('creado', auto_now=False,auto_now_add=True)
    edited = models.DateTimeField('editado', auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Usuario afectado'
        verbose_name_plural = 'Usuarios afectados'

    def __str__(self):
        return self.detalle    


class TipoSistema(models.Model):
    detalle = models.CharField('nombre',max_length=50)
    created = models.DateTimeField('creado', auto_now=False,auto_now_add=True)
    edited = models.DateTimeField('editado', auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Tipo de sistema'
        verbose_name_plural = 'Tipos de sistema'

    def __str__(self):
        return self.detalle     


class Estado(models.Model):
    detalle = models.CharField('nombre',max_length=50)
    created = models.DateTimeField('creado', auto_now=False,auto_now_add=True)
    edited = models.DateTimeField('editado', auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.detalle     


class Sistema(models.Model):
    nombre = models.CharField('nombre',max_length=50)
    created = models.DateTimeField('creado', auto_now=False,auto_now_add=True)
    edited = models.DateTimeField('editado', auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Sistema'
        verbose_name_plural = 'Sistemas'

    def __str__(self):
        return self.nombre    


class Participante(models.Model):
    nombre = models.CharField('nombre',max_length=50)
    cargo = models.CharField('cargo',max_length=50)
    email = models.EmailField(max_length=254)
    created = models.DateTimeField('creado', auto_now=False,auto_now_add=True)
    edited = models.DateTimeField('editado', auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'

    def __str__(self):
        return self.nombre + " - " + self.cargo

class Servidor(models.Model):
    nombre = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    estado = models.BooleanField()

    class Meta:
        verbose_name = 'Servidor'
        verbose_name_plural = 'Servidores'

    def __str__(self):
        return self.nombre


class Enlace(models.Model):
    ubicacion_origen = models.CharField(max_length=50)
    ubicacion_destino = models.CharField(max_length=50)
    caracteristicas = models.CharField(max_length=300)

    def __str__(self):
        return self.ubicacion_origen + " - " + self.ubicacion_destino

class Region(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    

class Ubicacion(models.Model):
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)


class Reporte(models.Model):
    detalle = models.CharField(max_length=300)
    resumen = models.CharField(max_length=100)
    impacto = models.CharField(max_length=100)
    fecha_conocimiento = models.DateTimeField()
    indisponibilidad = models.BooleanField()
    tiempo_indisponibilidad = models.DateTimeField()
    monitoreo = models.BooleanField()
    fecha_incidente = models.DateTimeField()
    fecha_restauracion = models.DateTimeField()
    ciberseguridad = models.BooleanField()
    causa_principal = models.CharField(max_length=100)
    solucion = models.CharField(max_length=300)
    analisis_posterior = models.CharField(max_length=100)
    control_de_cambios = models.CharField(max_length=200)
    ticket_OTRS = models.CharField(max_length=200)
    id_pais = models.ForeignKey(Pais,on_delete=models.CASCADE)
    id_causa = models.ForeignKey(Causa,on_delete=models.CASCADE)
    sistema_servicio = models.ForeignKey(SistemaServicio,on_delete=models.CASCADE)
    area_a_cargo = models.ForeignKey(AreaACargo,on_delete=models.CASCADE)
    agrupacion = models.ForeignKey(Agrupacion,on_delete=models.CASCADE)
    plataforma = models.ForeignKey(Plataforma,on_delete=models.CASCADE)
    alcance = models.ForeignKey(Alcance,on_delete=models.CASCADE)
    clasificacion_impacto = models.ForeignKey(ClasificacionImpacto,on_delete=models.CASCADE)
    tipo_solucion = models.ForeignKey(TipoSolucion,on_delete=models.CASCADE)
    via_conocimiento = models.ForeignKey(ViaConocimiento,on_delete=models.CASCADE)
    usuarios_afectados = models.ForeignKey(UsuariosAfectados,on_delete=models.CASCADE)
    tipo_sistema = models.ForeignKey(TipoSistema,on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    empresas_monitoreo = models.ManyToManyField(EmpresaMonitoreo)
    sistemas = models.ManyToManyField(Sistema)
    participantes = models.ManyToManyField(Participante)
    servidor = models.ManyToManyField(Servidor)
    enlace = models.ManyToManyField(Enlace)
    ubicacion = models.ManyToManyField(Ubicacion)
    created = models.DateTimeField('creado',auto_now=False,auto_now_add=True)
    edited = models.DateTimeField('editado',auto_now=True,auto_now_add=False)


    class Meta:
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'

    def __str__(self):
        return self.detalle


class AccionPreventiva(models.Model):
    detalle = models.CharField(max_length=100)
    reporte = models.ForeignKey(Reporte,on_delete=models.CASCADE)
    responsable = models.ForeignKey(Participante,on_delete=models.CASCADE)
    created = models.DateTimeField('creado', auto_now=False,auto_now_add=True)
    edited = models.DateTimeField('editado', auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Acción preventiva'
        verbose_name_plural = 'Acciones preventivas'

    def __str__(self):
        return self.detal

class MotivoIncidente(models.Model):
    motivo = models.CharField(max_length=100)
    reporte = models.ForeignKey(Reporte,on_delete=models.CASCADE)
    created = models.DateTimeField('creado', auto_now=False,auto_now_add=True)
    edited = models.DateTimeField('editado', auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Motivo incidente'
        verbose_name_plural = 'Motivos incidentes'

    def __str__(self):
        return self.motivo


class AccionIncidente(models.Model):
    accion = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    reporte = models.ForeignKey(Reporte,on_delete=models.CASCADE)
    created = models.DateTimeField('creado', auto_now=False,auto_now_add=True)
    edited = models.DateTimeField('editado', auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = 'Acción incidente'
        verbose_name_plural = 'Acciones incidentes'

    def __str__(self):
        return self.accion


class Seguimiento(models.Model):
    detalle = models.CharField(max_length=300)
    plazo = models.DateField()
    reporte = models.ForeignKey(Reporte,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Seguimiento'
        verbose_name_plural = 'Seguimientos'

    def __str__(self):
        return self.detalle