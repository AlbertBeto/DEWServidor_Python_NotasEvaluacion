from django.db import models

# UD6.6 6.6.c RA6.c Creo las funciones siguiendo el anexo IV
from core.models import Modulo, CritEvaluacion, ResAprendizaje
from programacion_didactica.models import InstEvaluacion, PondRA, PondCriterio, PondCritUD, Unidad

def get_modulod_all():
    return Modulo.objects.all()

def get_ie_3():
    return InstEvaluacion.objects.all()[:3]
 
def get_crit_min():
    return CritEvaluacion.objects.filter(minimo=True)

def get_ra_not_0612():
    return ResAprendizaje.objects.exclude(codigo__startswith='0612')

def get_ie_I1_defensa():
    return InstEvaluacion.objects.filter(codigo='I1', nombre__icontains='defensa')
# ID menor que 2 (lt), ordenador por codigo en descendente es con - delante de codigo
def get_mod_id_lt_2_cod_des():
    return Modulo.objects.filter(id__lt=2).order_by('-codigo')
# ID mayor que 2 (gt)
def get_mod_id_gt_2():
    return Modulo.objects.filter(id__gt=2)
#  Que nombre contiene desarrollo y ordenado por nombre. 
def get_mod_des_nom_des():
    return Modulo.objects.filter(nombre__icontains='desarrollo').order_by('nombre')
# Aquellos que no acabe el codigo en '1'
def get_ra_not_RA1():
    return ResAprendizaje.objects.exclude(codigo__endswith='1')
# Con get y sin values() recuperamos el objeto 
def get_ra_cli_RA3():
    return ResAprendizaje.objects.get(modulo__icontains='cliente', codigo__endswith='3')
#  filtramos Criteros de evaluacion por los que en el codigo de resultado de aprendizaje contenga un 06 y excluimos los nombre del modulo contenga cliente. 
def get_ce_RA06_not_cli():
    return CritEvaluacion.objects.filter(ResAprendizaje__codigo__icontains='06').exclude(ResAprendizaje__modulo__icontains='cliente')
# Utilizo la e en el gt para sea igual o mayor gt q 5.
def get_pon_ra_gt_5():
    return PondRA.objects.filter(porcentaje__gte='5')
# Utilizo range para filtrar dentro de rango.
def get_ce_5_10_RA1():
    return PondCriterio.objects.filter(porcentaje__range=(5,10),ResAprendizaje__codigo__endswith='1',Modulo__codigo='0613'                             )
# Utilizo create() y dando valores a los campos. 
def create_ie12():
    return InstEvaluacion.objects.create(codigo='I12', nombre="Nuevo instrumento 12",descripcion="Nuevo instrumento 12")
# No entiendo lo que me pide el enunciado. 
def create_ud15_pon():
    return PondCritUD
# Guardo la última unidad con last() y luego la updateo con save()
def update_last_ud():
    ultima_unidad = Unidad.objects.last()
    ultima_unidad = ultima_unidad+" (última)"
    ultima_unidad.save()
    return ultima_unidad
# No funciona FALTA TRABAJARLA
def update_ce_RA2_x2():
    PondCriterio.objects.filter(ResAprendizaje__codigo__endswith='2',Modulo__codigo="0613")
#FALTA EMPEZARLA
def update_pon_ce_RA1_div2():
    return

def delete_pon_ce_lt_5():
    return PondCriterio.objects.filter(porcentaje__lt=5).delete()

def delete_pon_ce_UD15():
    unidad_ud3 = Unidad.objects.get(nombre__icontains='UD3')
    return PondCritUD.objects.filter(unidad=unidad_ud3).delete()