from django.db import models

# Create your models here.
# UD6.3.a Creo los modelos siguiendo la tabla 1
# UD6.3.b Creo los str siguiendo tabla 2
class Unidad(models.Model):
    codigo = models.CharField(max_length = 4, unique=True)
    nombre = models.CharField(max_length = 256, unique=True)

    def __str__(self):
       return {self.codigo}'-'{self.nombre}

class InstEvaluacion(models.Model):
    codigo = models.CharField(max_length = 4, unique=True)
    nombre = models.CharField(max_length = 256, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return {self.codigo}'-'{self.nombre}

class PondRA(models.Model):
    resultado_aprendizaje = models.ForeignKey(ResAprendizaje,on_delete=models.PROTECT)
    porcentaje = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0.0)

    def __str__(self):
        return {str(self.resultado_aprendizaje)}'-'{str(self.porcentaje)}

class PondCriterio(models.Model):
    criterio_evaluacion = models.ForeignKey(CritEvaluacion,on_delete=models.PROTECT)
    porcentaje = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0.0)
    
    def __str__(self):
        return {str(self.criterio_evaluacion)}'-'{self.porcentaje}


class PondCritUD(models.Model):
    criterio_evaluacion = models.ForeignKey(CritEvaluacion,on_delete=models.PROTECT)
    unidad = models.ForeignKey(Unidad,on_delete=models.PROTECT)
    porcentaje = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0.0)

    def __str__(self):
        return {str(self.unidad)}':'{str(self.criterio_evaluacion)}'-('+self.porcentaje+')'