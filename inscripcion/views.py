from django.shortcuts import render

# Create your views here.
def pre_inscripcion(request):
    return render(request,"inscripcion/pre_inscripcion.html")
def lista(request):
    return render(request,"inscripcion/lista.html")