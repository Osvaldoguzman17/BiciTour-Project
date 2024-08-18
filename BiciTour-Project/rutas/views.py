from django.shortcuts import render

from .models import Ruta,RutaRealizada

from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def proximos(request):
    if request.user.is_authenticated:
        rutas_proximas = Ruta.objects.filter(status='activa', fecha__gte=timezone.now().date()).exclude(rutarealizada__usuario=request.user)
    else:
        rutas_proximas = Ruta.objects.filter(status='activa', fecha__gte=timezone.now().date())
    return render(request, 'rutas/proximos.html', {'rutas_proximas': rutas_proximas})

@login_required
def realizados(request):
    rutas_realizadas = RutaRealizada.objects.all()
    return render(request, 'rutas/realizados.html', {'rutas_realizadas': rutas_realizadas})

def personalizada(request):
    ciudad = request.GET.get('ciudad', '')
    estado = request.GET.get('estado', '')
    duracion = request.GET.get('duracion', '')
    distancia = request.GET.get('distancia', '')

    recomendaciones = Ruta.objects.filter(status='activa')
    if ciudad:
        recomendaciones = recomendaciones.filter(ciudad__icontains=ciudad)
    if estado:
        recomendaciones = recomendaciones.filter(estado__icontains=estado)
    if duracion:
        try:
            duracion = float(duracion)
            recomendaciones = recomendaciones.filter(duracion__lte=duracion)
        except ValueError:
            pass  
    if distancia:
        try:
            distancia = float(distancia)
            recomendaciones = recomendaciones.filter(distancia__lte=distancia)
        except ValueError:
            pass  

    return render(request, 'rutas/personalizada.html', {
        'recomendaciones': recomendaciones
    })


def busqueda(request):
    query = request.GET.get('query', '')
    rutas = Ruta.objects.filter(nombre__icontains=query, status='activa')
    return render(request, 'rutas/busqueda.html', {'rutas': rutas, 'query': query})

def detalles(request, ruta_id):
    ruta = get_object_or_404(Ruta, id=ruta_id)
    return render(request, 'rutas/detalles.html', {'ruta': ruta})

def detalles_final(request, ruta_id):
    ruta = get_object_or_404(Ruta, id=ruta_id)
    return render(request, 'rutas/detalles_final.html', {'ruta': ruta})


def marcar_ruta_realizada(request, ruta_id):
    ruta = get_object_or_404(Ruta, id=ruta_id)

    if ruta.fecha and ruta.fecha <= timezone.now().date():
        ruta.status = False
        ruta.save()
        RutaRealizada.objects.create(usuario=request.user, ruta=ruta)

    else:
        ruta.status = False 
        ruta.save()
        RutaRealizada.objects.create(usuario=request.user, ruta=ruta)

    return redirect('Proximos')


def pre_inscripcion(request):
    return render(request,"inscripcion/pre_inscripcion.html")
def lista(request):
    return render(request,"inscripcion/lista.html")


