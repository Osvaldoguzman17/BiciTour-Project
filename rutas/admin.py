from django.contrib import admin
from .models import Ruta, RutaRealizada

@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'distancia', 'imagen')
    list_filter = ('distancia',)
    search_fields = ('nombre', 'descripcion')

@admin.register(RutaRealizada)
class RutaRealizadaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'ruta', 'fecha_realizacion')
    list_filter = ('fecha_realizacion', 'usuario', 'ruta')
    search_fields = ('usuario__username', 'ruta__nombre')
