# forms.py

from django import forms
from .models import RutaRealizada

class RutaRealizadaForm(forms.ModelForm):
    class Meta:
        model = RutaRealizada
        fields = ['fecha_realizacion']
        widgets = {
            'fecha_realizacion': forms.DateInput(attrs={'type': 'date'}),
        }
