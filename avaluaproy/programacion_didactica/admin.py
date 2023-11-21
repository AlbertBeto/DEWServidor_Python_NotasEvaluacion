from django.contrib import admin

# Register your models here.


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
    search_fields = ['codigo','descripcion',]
    preserve_filters = [True,]