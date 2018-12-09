from django.db import models
from django.utils import timezone

#Permisos DJANGO 
from django.utils.translation import ugettext as _


class OrdenTrabajo (models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Folio = models.CharField(primary_key=True, max_length=5)
    Cliente = models.CharField(max_length=40, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora_inicio = models.DateTimeField(blank=True, null=True)
    hora_termino = models.DateTimeField(blank=True, null=True)
    Id_ascensor =  models.CharField(max_length=40,blank=True, null=True)
    modelo_ascensor = models.CharField(max_length=200, blank=True, null=True)
    fallas = models.CharField(max_length=200)
    piezas_cambiadas = models.CharField(max_length=200)
    Nombre_Tecnico = models.CharField(max_length=200, blank=True, null=True)
    

    def __str__(self):
        return self.Folio

    def publish(self):
        self.fecha = timezone.now()
        self.save()

class RegistroCliente (models.Model):
    Nombre_Completo = models.CharField(max_length=200, blank=True, null=True)
    Direccion = models.CharField(max_length=200, blank=True, null=True)
    Ciudad = models.CharField(max_length=200, blank=True, null=True)
    Comuna = models.CharField(max_length=200, blank=True, null=True)
    Correo = models.EmailField(blank=True, null=True)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.Nombre_Completo

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

