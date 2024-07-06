from django.contrib import admin
from django.urls import path
from inicio import views  # Asegúrate de que esto es correcto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name='Principal'),  # Asegúrate de que 'principal' esté en views.py
    path('login/', views.login, name='Login'),  # Asegúrate de que 'login' esté en views.py
    path('registrar/', views.registrar, name='Registrar'),  # Asegúrate de que 'registrar' esté en views.py
    path('nueva_contraseña/', views.nueva_contraseña, name='Nueva Contraseña'),  # Asegúrate de que 'nueva_contraseña' esté en views.py
]
