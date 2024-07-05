from django.shortcuts import render, HttpResponse

# Create your views here.
def principal(request):
    return render(request,"inicio/principal.html")
    
def login(request):
    return render(request,"inicio/login.html")
def registrar(request):
    return render(request,"inicio/registrar.html")
def nueva_contraseña(request):
    return render(request,"inicio/nueva_contraseña.html")
    
    