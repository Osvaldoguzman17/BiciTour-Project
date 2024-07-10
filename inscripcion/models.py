from django.db import models

# Create your models here.
from django.db import models

class registroInscripcion(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="clave")
    nombre = models.CharField(max_length=15)
    correo = models.EmailField()
    telefono=models.IntegerField()
    estado=models.CharField(max_length=15)
    ciudad=models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name = "registroInscripcion"
        verbose_name_plural = "registroInscripciones"
        ordering = ["-created"]

    def _str_(self):
        return self.nombre