# urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from inicio.views import (principal, login, registrar, nueva_contraseña, recorridos, 
                          recorridos_realizados, recorridos_proximos, recomendaciones_personalizadas, 
                          contactanos, search, ruta_detail, marcar_ruta_realizada)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', principal, name='Principal'),
    path('login/', login, name='Login'),
    path('registrar/', registrar, name='Registrar'),
    path('nueva_contraseña/', nueva_contraseña, name='Nueva Contraseña'),
    path('recorridos/', recorridos, name='Recorridos'),
    path('recorridos_realizados/', recorridos_realizados, name='Recorridos Realizados'),
    path('recorridos_proximos/', recorridos_proximos, name='Recorridos Próximos'),
    path('recomendaciones_personalizadas/', recomendaciones_personalizadas, name='Recomendaciones Personalizadas'),
    path('contactanos/', contactanos, name='Contactanos'),
    path('search/', search, name='search'),
    path('ruta/<int:ruta_id>/', ruta_detail, name='ruta_detail'),
    path('marcar_ruta_realizada/<int:ruta_id>/', marcar_ruta_realizada, name='marcar_ruta_realizada'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
