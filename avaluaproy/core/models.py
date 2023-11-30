from django.db import models
#from programacion_didactica.models import PondCriterio


# Create your models here.
# UD6.3.a Creo los modelos siguiendo la tabla 1
# UD6.3.b Creo los str siguiendo tabla 2
class Modulo(models.Model):
    codigo = models.CharField(max_length = 10, verbose_name = "codigo", unique=True)
    nombre = models.CharField(max_length = 256, verbose_name = "nombre", unique=True)

    def __str__(self):
        return self.nombre
    class Meta:
        # UD6.4.e Doy valores a verbose_name y verbose_name_plural
        verbose_name = "Modulo"
        verbose_name_plural = "Modulos"
        # UD6.4.f Incorporo el ordering
        ordering = ['codigo']

class ResAprendizaje(models.Model):
    modulo = models.ForeignKey(Modulo,on_delete=models.PROTECT)
    codigo = models.CharField(max_length = 10, verbose_name="codigo", unique=True)
    descripcion = models.TextField(verbose_name="Descripcion")

    def __str__(self):
        return f"{self.codigo}.{self.descripcion[:100]}"
    # UD6.3.c Incluir clase meta y unique_together con los valores tabla 3
    class Meta:
        unique_together =[["modulo","codigo"]]
        # UD6.4.e Doy valores a verbose_name y verbose_name_plural
        verbose_name = "Resultado de aprendizaje"
        verbose_name_plural = "Resultados de aprendizaje"
        # UD6.4.f Incorporo el ordering
        ordering = ['codigo']


class CritEvaluacion(models.Model):
    resultado_aprendizaje = models.ForeignKey(ResAprendizaje,on_delete=models.PROTECT)
    codigo = models.CharField(max_length = 4, verbose_name="codigo")
    descripcion = models.TextField()
    minimo = models.BooleanField()

    def __str__(self):
        return f"{self.resultado_aprendizaje.codigo}.{self.codigo} - {self.descripcion[:100]}"
    # UD6.3.c Incluir clase meta y unique_together con los valores tabla 3
    class Meta:
        unique_together =[["resultado_aprendizaje","codigo"]]
        # UD6.4.e Doy valores a verbose_name y verbose_name_plural
        verbose_name = "Criterio de evaluación"
        verbose_name_plural = "Criterios de evaluación"
        # UD6.4.f Incorporo el ordering
        ordering = ['resultado_aprendizaje__codigo'] #, 'criterio_evaluacion__codigo']