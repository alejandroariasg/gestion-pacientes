from django.db import models

# Create your models here.

class FaltaProgramarCita(models.Model):
    numero_documento = models.CharField(max_length = 25, blank=True)
    nombre = models.CharField(max_length = 60, null=True)
    primer_apellido = models.CharField(max_length = 60, null=True)
    segundo_apellido = models.CharField(max_length = 60, null=True)
    dx = models.CharField(max_length = 60, null=True)
    telefono = models.CharField(max_length = 100, null=True)
    lugar_residencia = models.CharField(max_length = 50, null=True)
    observaciones = models.TextField(null=True)
    fecha_hora = models.DateTimeField(null=True)
    psiquiatra = models.CharField(max_length = 50, null=True)
    fecha_creacion = models.DateField(null=True,blank=True)
    fecha_actualizacion = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length = 10, null=True)
    edad = models.IntegerField(null=True)
    dia = models.CharField(max_length = 50, null=True)
    estado = models.IntegerField(null=True, blank=True)