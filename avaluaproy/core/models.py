from django.db import models

# Create your models here.
class Modulo(models.Model):
    codigo = models.CharField(max_length = 10, verbose_name = "codigo", unique=True)
    nombre = models.CharField(max_length = 256, verbose_name = "nombre", unique=True)

class ResAprendizaje(models.Model):
    modulo = models.ForeignKey(Modulo,on_delete=models.PROTECT, unique=True)
    codigo = models.CharField(max_length = 10, verbose_name="codigo")
    descripcion = models.Textfield()

class CritEvaluacion(models.Model):
    resultado_aprendizaje = models.ForeignKey(ResAprendizaje,on_delete=models.PROTECT)
    codigo = models.CharField(max_length = 4, verbose_name="codigo")
    descripcion = models.Textfield()
    minimo = models.BooleanField()