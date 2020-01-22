from django.db import models

# Create your models here.

class FaltaProgramarCita(models.Model):
    numero_documento = models.CharField(max_length = 25)
    nombre = models.CharField(max_length = 60, blank=True)
    primer_apellido = models.CharField(max_length = 60, blank=True)
    segundo_apellido = models.CharField(max_length = 60, blank=True)
    dx = models.CharField(max_length = 60, blank=True)
    telefono = models.CharField(max_length = 100, blank=True)
    lugar_residencia = models.CharField(max_length = 50, blank=True)
    observaciones = models.TextField(blank=True)
    fecha_hora = models.DateTimeField(blank=True)
    psiquiatra = models.CharField(max_length = 50, blank=True)
    fecha_creacion = models.DateField(blank=True)
    fecha_actualizacion = models.DateField(blank=True)
    sexo = models.CharField(max_length = 10, blank=True)
    edad = models.IntegerField(blank=True)
    dia = models.CharField(max_length = 50, blank=True)
    estado = models.IntegerField(blank=True)