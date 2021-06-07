from typing import Text
from django.test import TestCase
from .models import (
                    Pais,Causa,SistemaServicio,AreaACargo,EmpresaMonitoreo,Agrupacion,Plataforma,
                    Alcance,ClasificacionImpacto,TipoSolucion,ViaConocimiento,UsuariosAfectados,
                    TipoSistema,Estado,Sistema,Participante,Servidor,Enlace,Region,Comuna,Ubicacion,
                    Reporte,AccionPreventiva,MotivoIncidente,AccionIncidente,Seguimiento
                    )

# Create your tests here.
class PaisTestCase(TestCase):

    def setUp(self):
        Pais.objects.create(nombre="Chile")
        Pais.objects.create(nombre="Perú")

    def test_get_pais(self):
        pais = Pais.objects.get(nombre="Chile")
        pais2 = Pais.objects.get(nombre="Perú")


class CausaTestCase(TestCase):

    def setUp(self):
        Causa.objects.create(nombre="Prueba 1")
        Causa.objects.create(nombre="Prueba 2")

    def test_get_causa(self):
        elemento = Causa.objects.get(nombre="Prueba 1")
        elemento2 = Causa.objects.get(nombre="Prueba 2")


class SistemaServicioTestCase(TestCase):

    def setUp(self):
        SistemaServicio.objects.create(nombre="Prueba sistema 1")
        SistemaServicio.objects.create(nombre="Prueba sistema 2")

    def test_get_sistemaServicio(self):
        elemento = SistemaServicio.objects.get(nombre="Prueba sistema 1")
        elemento2 = SistemaServicio.objects.get(nombre="Prueba sistema 2")

class AreaACargoTestCase(TestCase):

    def setUp(self):
        AreaACargo.objects.create(nombre="Prueba area 1")
        AreaACargo.objects.create(nombre="Prueba area 2")

    def test_get_areaACargo(self):
        elemento = AreaACargo.objects.get(nombre="Prueba area 1")
        elemento2 = AreaACargo.objects.get(nombre="Prueba area 2")


class EmpresaMonitoreoTestCase(TestCase):

    def setUp(self):
        EmpresaMonitoreo.objects.create(nombre="Prueba empresa 1")
        EmpresaMonitoreo.objects.create(nombre="Prueba empresa 2")

    def test_get_empresaMonitoreo(self):
        elemento = EmpresaMonitoreo.objects.get(nombre="Prueba empresa 1")
        elemento2 = EmpresaMonitoreo.objects.get(nombre="Prueba empresa 2")


class AgrupacionTestCase(TestCase):

    def setUp(self):
        Agrupacion.objects.create(nombre="Prueba agrupacion 1")
        Agrupacion.objects.create(nombre="Prueba agrupacion 2")

    def test_get_agrupacion(self):
        element = Agrupacion.objects.get(nombre="Prueba agrupacion 1")
        element2 = Agrupacion.objects.get(nombre="Prueba agrupacion 2")


class PlataformaTestCase(TestCase):

    def setUp(self):
        Plataforma.objects.create(nombre="Prueba plataforma 1")
        Plataforma.objects.create(nombre="Prueba plataforma 2")

    def test_get_plataforma(self):
        element = Plataforma.objects.get(nombre="Prueba plataforma 1")
        element2 = Plataforma.objects.get(nombre="Prueba plataforma 2")


class AlcanceTestCase(TestCase):

    def setUp(self):
        Alcance.objects.create(detalle="Prueba alcance 1")
        Alcance.objects.create(detalle="Prueba alcance 2")

    def test_get_alcance(self):
        element = Alcance.objects.get(detalle="Prueba alcance 1")
        element2 = Alcance.objects.get(detalle="Prueba alcance 2")


class clasificacionImpactoTestCase(TestCase):

    def setUp(self):
        ClasificacionImpacto.objects.create(detalle="Prueba clasificacion 1")
        ClasificacionImpacto.objects.create(detalle="Prueba clasificacion 2")

    def test_get_clasificacionImpacto(self):
        element = ClasificacionImpacto.objects.get(detalle="Prueba clasificacion 1")
        element2 = ClasificacionImpacto.objects.get(detalle="Prueba clasificacion 2")


class tipoSolucionTestCase(TestCase):

    def setUp(self):
        TipoSolucion.objects.create(detalle="Prueba solucion 1")
        TipoSolucion.objects.create(detalle="Prueba solucion 2")

    def test_get_tipoSolucion(self):
        element = TipoSolucion.objects.get(detalle="Prueba solucion 1")
        element2 = TipoSolucion.objects.get(detalle="Prueba solucion 2")


class viaConocimientoTestCase(TestCase):

    def setUp(self):
        ViaConocimiento.objects.create(detalle="Prueba via conocimiento 1")
        ViaConocimiento.objects.create(detalle="Prueba via conocimiento 2")

    def test_get_viaConocimiento(self):
        element = ViaConocimiento.objects.get(detalle="Prueba via conocimiento 1")
        element2 = ViaConocimiento.objects.get(detalle="Prueba via conocimiento 2")


class usuariosAfectadosTestCase(TestCase):

    def setUp(self):
        UsuariosAfectados.objects.create(detalle="Prueba usuarios afectados 1")
        UsuariosAfectados.objects.create(detalle="Prueba usuarios afectados 2")

    def test_get_usuariosAfectados(self):
        element = UsuariosAfectados.objects.get(detalle="Prueba usuarios afectados 1")
        element2 = UsuariosAfectados.objects.get(detalle="Prueba usuarios afectados 2")


class tipoSistemaTestCase(TestCase):

    def setUp(self):
        TipoSistema.objects.create(detalle="Prueba sistema 1")
        TipoSistema.objects.create(detalle="Prueba sistema 2")

    def test_get_tipoSistema(self):
        element = TipoSistema.objects.get(detalle="Prueba sistema 1")
        element2 = TipoSistema.objects.get(detalle="Prueba sistema 2")


class EstadoTestCase(TestCase):

    def setUp(self):
        Estado.objects.create(detalle="Prueba estado 1")
        Estado.objects.create(detalle="Prueba estado 2")

    def test_get_estado(self):
        element = Estado.objects.get(detalle="Prueba estado 1")
        element2 = Estado.objects.get(detalle="Prueba estado 2")


class SistemaTestCase(TestCase):

    def setUp(self):
        Sistema.objects.create(nombre="Prueba sistema 1")
        Sistema.objects.create(nombre="Prueba sistema 2")

    def test_get_sistema(self):
        element = Sistema.objects.get(nombre="Prueba sistema 1")
        element2 = Sistema.objects.get(nombre="Prueba sistema 2")


class ParticipanteTestCase(TestCase):

    def setUp(self):
        Participante.objects.create(nombre="Nombre 1",cargo="Cargo 1",email="prueba@gmail.com")
        Participante.objects.create(nombre="Nombre 2",cargo="Cargo 2",email="prueba2@gmail.com")

    def test_get_participante(self):
        element = Participante.objects.get(nombre="Nombre 1")
        element2 = Participante.objects.get(nombre="Nombre 2")


class ServidorTestCase(TestCase):

    def setUp(self):
        Servidor.objects.create(nombre="Servidor 1",ip="ip 1",estado=True)
        Servidor.objects.create(nombre="Servidor 2",ip="ip 2",estado=False)

    def test_get_servidor(self):
        element=Servidor.objects.get(nombre="Servidor 1")
        element=Servidor.objects.get(estado=False)


class EnlaceTestCase(TestCase):

    def setUp(self):
        Enlace.objects.create(ubicacion_origen="Origen 1",ubicacion_destino="Destino 1",
                                caracteristicas="Caracteristicas 1")
        Enlace.objects.create(ubicacion_origen="Origen 2",ubicacion_destino="Destino 2",
                                caracteristicas="Caracteristicas 2")

    def test_get_enlace(self):
        element=Enlace.objects.get(ubicacion_origen="Origen 1")
        element2=Enlace.objects.get(ubicacion_destino="Destino 2")


class UbicacionTestCase(TestCase):

    def setUp(self):
        Region.objects.create(nombre="Region Metropolitana")
        Region.objects.create(nombre="Region de Los Lagos")        
        Comuna.objects.create(nombre="San Bernardo",region_id=1)
        Comuna.objects.create(nombre="Dalcahue",region_id=2)        
        Ubicacion.objects.create(comuna_id=1,direccion="Direccion 1",descripcion="Descripcion 1")
        Ubicacion.objects.create(comuna_id=2,direccion="Direccion 2",descripcion="Descripcion 2")

    def test_get_ubicacion(self):
        elemen=Ubicacion.objects.get(id=1)
        element1=Ubicacion.objects.get(direccion="Direccion 1")    