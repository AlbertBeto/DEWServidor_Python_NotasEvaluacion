from django.db import models

# Create your models here.
class Unidad(models.Model):
    codigo = models.CharField(max_length = 4, unique=True)
    nombre = models.CharField(max_length = 256, unique=True)

class InstEvaluacion(models.Model):
    codigo = models.CharField(max_length = 4, unique=True)
    nombre = models.CharField(max_length = 256, unique=True)
    descripcion = models.TextField()

class PondRA(models.Model):
    resultado_aprendizaje = models.ForeignKey(ResAprendizaje,on_delete=models.PROTECT)
    porcentaje = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0.0)