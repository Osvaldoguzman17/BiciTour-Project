from django.shortcuts import get_object_or_404, render, redirect
from .models import Ruta, RutaRealizada
from django.contrib.auth.models import User  # Asegúrate de importar User

def principal(request):
    return render(request, "inicio/principal.html")

def login(request):
    return render(request, "inicio/login.html")

def registrar(request):
    return render(request, "inicio/registrar.html")

def nueva_contraseña(request):
    return render(request, "inicio/nueva_contraseña.html")

def recorridos(request):
    return render(request, "inicio/recorridos.html")

def recorridos_realizados(request):
    rutas_realizadas = RutaRealizada.objects.filter(usuario=request.user)  # Filtra por usuario autenticado
    return render(request, 'inicio/recorridos_realizados.html', {'rutas_realizadas': rutas_realizadas})

def recorridos_proximos(request):
    if request.user.is_authenticated:
        # Recupera todas las rutas que aún no han sido realizadas por el usuario
        rutas_proximas = Ruta.objects.exclude(rutarealizada__usuario=request.user)
    else:
        # Si el usuario no está autenticado, muestra todas las rutas
        rutas_proximas = Ruta.objects.all()
    return render(request, 'inicio/recorridos_proximos.html', {'rutas_proximas': rutas_proximas})

def recomendaciones_personalizadas(request):
    return render(request, "inicio/recomendaciones_personalizadas.html")

def contactanos(request):
    return render(request, "inicio/contactanos.html")

def search(request):
    query = request.GET.get('query', '')
    rutas = Ruta.objects.filter(nombre__icontains=query)
    return render(request, 'inicio/search_results.html', {'rutas': rutas, 'query': query})

def ruta_detail(request, ruta_id):
    ruta = get_object_or_404(Ruta, id=ruta_id)
    return render(request, 'inicio/ruta_detail.html', {'ruta': ruta})

# views.py
from django.shortcuts import redirect, get_object_or_404
from .models import Ruta, RutaRealizada

# views.py
from django.shortcuts import redirect, get_object_or_404
from .models import Ruta, RutaRealizada

def marcar_ruta_realizada(request, ruta_id):
    ruta = get_object_or_404(Ruta, id=ruta_id)
    
    if request.user.is_authenticated:
        # Crear un nuevo registro en RutaRealizada
        RutaRealizada.objects.get_or_create(usuario=request.user, ruta=ruta)  # Usa get_or_create para evitar duplicados
        # Redirige al usuario a la página de recorridos realizados después de marcar la ruta
        return redirect('Recorridos Realizados')
    
    return redirect('Principal')
