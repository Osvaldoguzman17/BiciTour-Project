# forms.py

from django import forms
from .models import registroUsuario, RutaRealizada

# Formulario para el registro de usuario
class registroUsuarioForm(forms.ModelForm):
    class Meta:
        model = registroUsuario
        fields = ['correo', 'nombre', 'contraseña']
        widgets = {
            'contraseña': forms.PasswordInput(),  # Asegúrate de usar un widget de contraseña para este campo
        }

# Formulario para registrar una ruta realizada
class RutaRealizadaForm(forms.ModelForm):
    class Meta:
        model = RutaRealizada
        fields = ['fecha_realizacion']
        widgets = {
            'fecha_realizacion': forms.DateInput(attrs={'type': 'date'}),
        }

