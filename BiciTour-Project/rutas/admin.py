from django.contrib import admin
from .models import Ruta, RutaRealizada
from django.utils.html import format_html

# Register your models here.

class RutaAdmin(admin.ModelAdmin):
    list_display = ('icono','id','nombre', 'descripcion', 'distancia', 'imagen','dificultad')
    list_filter = ('distancia',)
    search_fields = ('nombre', 'descripcion')


    #Agregar nuevas modificaciones al admin de django

    #1
    list_editable = ('nombre',)

    #2
    def icono(self, obj):
        return format_html('<svg width="16" height="16" fill="currentColor" class="bi bi-house" viewBox="0 0 16 16"><path d="M8 3.293l5 5V15h-3V9H6v6H3V8.293l5-5z"/></svg>')
    
    #3
    def dificultad(self, obj):
        if obj.distancia <= 5:
         return "Fácil"
        elif 5 < obj.distancia <= 10:
         return "Media"
        else:
         return "Difícil"
    dificultad.short_description = 'Dificultad'

    #4
    list_display_links = ('id','icono',)












    

admin.site.register(Ruta, RutaAdmin)
    

class RutaRealizadaAdmin(admin.ModelAdmin):
    #list_display = ('usuario', 'ruta', 'fecha_realizacion')
    #list_filter = ('fecha_realizacion', 'usuario', 'ruta')
    search_fields = ('usuario_username', 'ruta_nombre')

    
admin.site.register(RutaRealizada, RutaRealizadaAdmin)