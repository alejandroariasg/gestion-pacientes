from django.db import models

# Create your models here.

class FaltaPorgramarCita(models.Model):
    numero_documento = models.CharField(max_length = 25)
    nombre = models.CharField(max_length = 60)
    primer_apellido = models.CharField(max_length = 60)
    segundo_apellido = models.CharField(max_length = 60)
    dx = models.CharField(max_length = 60)
    telefono = models.CharField(max_length = 100)
    lugar_residencia = models.CharField(max_length = 50)
    observaciones = models.TextField()
    fecha_hora = models.DateTimeField()
    psiquiatra = models.CharField(max_length = 50)
    fecha_creacion = models.DateField()
    fecha_actualizacion = models.DateField()
    sexo = models.CharField(max_length = 10)
    edad = models.IntegerField()
    dia = models.CharField(max_length = 50)
    estado = models.IntegerField()