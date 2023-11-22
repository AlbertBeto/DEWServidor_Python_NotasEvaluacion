from django.contrib import admin

# Register your models here.
# 6.4.c Implemento las clases según Anexo II
from .models import Unidad, InstEvaluacion, PondRA, PondCriterio, PondCritUD

class UnidadAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('codigo', 'nombre',)
    search_fields = ['codigo','nombre',]
    #Con el - delante del campo le digo que lo ordene en descendente
    ordering = ['-id',]

class InstEvalAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('codigo','nombre',)
    search_fields = ['codigo','nombre',]

class PondRAAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('resultado_aprendizaje','porcentaje',)
    list_filter = ('resultado_aprendizaje',)
    #Con la __ vinculamos la busqueda con el resultado. 
    search_fields = ['resultado_aprendizaje__codigo','resultado_aprendizaje__descripcion',]
    preserve_filters = [True,]

class PondCritAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('criterio_evaluacion','porcentaje',)
    #posible error.
    list_filter = ('criterio_evaluacion__resultado_aprendizaje',)
    search_fields = ['criterio_evaluacion__codigo','criterio_evaluacion__descripcion','criterio_evaluacion__resultado_aprendizaje__codigo','criterio_evaluacion__resultado_aprendizaje__descripcion',]
    preserve_filters = [True,]

class PondCritUDAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('unidad','criterio_evaluacion','porcentaje',)
    #posible error.
    list_filter = ('resultado_aprendizaje', 'unidad')
    search_fields = ['criterio_evaluacion__codigo','criterio_evaluacion__descripcion','criterio_evaluacion__resultado_aprendizaje__codigo','criterio_evaluacion__resultado_aprendizaje__descripcion','unidad__nombre',]
    preserve_filters = [True,]


admin.site.register(Unidad, UnidadAdmin)
admin.site.register(InstEvaluacion, InstEvalAdmin)
admin.site.register(PondRA, PondRAAdmin)
admin.site.register(PondCriterio, PondCritAdmin)
admin.site.register(PondCritUD, PondCritUDAdmin)