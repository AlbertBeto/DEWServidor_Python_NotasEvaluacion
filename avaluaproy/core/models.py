from django.db import models

# Create your models here.
# UD6.3.a Creo los modelos siguiendo la tabla 1
# UD6.3.b Creo los str siguiendo tabla 2
class Modulo(models.Model):
    codigo = models.CharField(max_length = 10, verbose_name = "codigo", unique=True)
    nombre = models.CharField(max_length = 256, verbose_name = "nombre", unique=True)

    def __str__(self):
        return self.nombre

class ResAprendizaje(models.Model):
    modulo = models.ForeignKey(Modulo,on_delete=models.PROTECT, unique=True)
    codigo = models.CharField(max_length = 10, verbose_name="codigo")
    descripcion = models.Textfield()

    def __str__(self):
        return {self.codigo}'.'{self.descripcion[:100]}
    # UD6.3.c Incluir clase meta y unique_together con los valores tabla 3
    class Meta:
        unique_together =[[modulo,codigo]]

class CritEvaluacion(models.Model):
    resultado_aprendizaje = models.ForeignKey(ResAprendizaje,on_delete=models.PROTECT)
    codigo = models.CharField(max_length = 4, verbose_name="codigo")
    descripcion = models.Textfield()
    minimo = models.BooleanField()

     def __str__(self):
        return {self.resultado_aprendizaje}'.'{self.codigo}'.'{self.descripcion[:100]}
    # UD6.3.c Incluir clase meta y unique_together con los valores tabla 3
    class Meta:
        unique_together =[[resultado_aprendizaje,codigo]]