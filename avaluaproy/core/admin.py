from django.contrib import admin

# Register your models here.
# 6.4.b Implemento las clases según Anexo II
from .models import Modulo, ResAprendizaje, CritEvaluacion

class ModuloAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('id','codigo','nombre',)
    search_fields = ['codigo','nombre',]
    readonly_fields = ['id',]

class ResAprendizajeAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('codigo','modulo','descripcion',)
    list_filter = ('modulo',)
    search_fields = ['codigo','descripcion',]
    preserve_filters = [True,]

class CritEvaluacionAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('resultado_aprendizaje','codigo','descripcion','minimo',)
    list_filter = ('resultado_aprendizaje','minimo',)
    search_fields = ['codigo','resultado_aprendizaje','descripcion',]
    preserve_filters = [True,]

admin.site.register(Modulo, ModuloAdmin)
admin.site.register(ResAprendizaje, ResAprendizajeAdmin)
admin.site.register(CritEvaluacion, CritEvaluacionAdmin)