from django.contrib import admin
from .models import registroUsuario, Ruta, RutaRealizada

# Admin configuration for registroUsuario
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'nombre', 'correo')
    search_fields = ('id', 'nombre', 'correo')
    date_hierarchy = 'created'
    list_filter = ('nombre', 'correo')

admin.site.register(registroUsuario, AdministrarModelo)

# Admin configuration for Ruta
@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'distancia', 'imagen')
    list_filter = ('distancia',)
    search_fields = ('nombre', 'descripcion')

# Admin configuration for RutaRealizada
@admin.register(RutaRealizada)
class RutaRealizadaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'ruta', 'fecha_realizacion')
    list_filter = ('fecha_realizacion', 'usuario', 'ruta')
    search_fields = ('usuario__username', 'ruta__nombre')

