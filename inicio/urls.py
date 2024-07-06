from django.contrib import admin
from django.urls import path
from inicio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name='Principal'),
    path('login/', views.login, name='Login'),
    path('registrar/', views.registrar, name='Registrar'),
    path('nueva_contraseña/', views.nueva_contraseña, name='Nueva Contraseña'),
]
