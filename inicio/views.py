from django.shortcuts import render, redirect
from .forms import registroUsuarioForm

def principal(request):
    return render(request, "inicio/principal.html")
    
def login(request):
    return render(request, "inicio/login.html")

def registrar(request):
    if request.method == 'POST':
        form = registroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Principal')  # Redirigir a la página principal u otra página después de registrarse
    else:
        form = registroUsuarioForm()
    return render(request, 'inicio/registrar.html', {'form': form})

def nueva_contraseña(request):
    return render(request, "inicio/nueva_contraseña.html")
