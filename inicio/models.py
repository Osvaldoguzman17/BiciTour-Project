# models.py
from django.db import models
from django.contrib.auth.models import User  # Asegúrate de importar el modelo User

# Modelo para registro de usuarios
class registroUsuario(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="clave")
    correo = models.TextField()
    nombre = models.TextField()
    contraseña = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "registroUsuario"
        verbose_name_plural = "registroUsuarios"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre

# Modelo para rutas
class Ruta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    distancia = models.FloatField()
    imagen = models.ImageField(upload_to='rutas/', blank=True, null=True)
    
    def __str__(self):
        return self.nombre

# Modelo para rutas realizadas
class RutaRealizada(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Aquí usamos el modelo User
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, related_name='rutarealizada')  # Usamos 'rutarealizada' como related_name
    fecha_realizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.ruta.nombre}"
