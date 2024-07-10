from django.shortcuts import render

from .models import Ruta,RutaRealizada

from django.shortcuts import get_object_or_404, render, redirect

def realizados(request):
    rutas_realizadas = RutaRealizada.objects.filter(usuario=request.user)
    return render(request, 'rutas/realizados.html', {'rutas_realizadas': rutas_realizadas})

def proximos(request):
    if request.user.is_authenticated:
        rutas_proximas = Ruta.objects.exclude(rutarealizada__usuario=request.user)
    else:
        rutas_proximas = Ruta.objects.all()
    return render(request, 'rutas/proximos.html', {'rutas_proximas': rutas_proximas})

def personalizada(request):
    query = request.GET.get('query', '')
    if query:
        recomendaciones = Ruta.objects.filter(nombre__icontains=query)
    else:
        recomendaciones = Ruta.objects.all()  
    return render(request, 'rutas/personalizada.html', {'recomendaciones': recomendaciones, 'query': query})

def busqueda(request):
    query = request.GET.get('query', '')
    rutas = Ruta.objects.filter(nombre__icontains=query)
    return render(request, 'rutas/busqueda.html', {'rutas': rutas, 'query': query})

def detalles(request, ruta_id):
    ruta = get_object_or_404(Ruta, id=ruta_id)
    return render(request, 'rutas/detalles.html', {'ruta': ruta})

def marca_ruta_realizada(request, ruta_id):
    ruta = get_object_or_404(Ruta, id=ruta_id)
    
    if request.user.is_authenticated:
        RutaRealizada.objects.get_or_create(usuario=request.user, ruta=ruta) 
        return redirect('Realizados')
    
    return redirect('Principal')


