
from django.shortcuts import render,redirect
from django.utils import timezone
from rutas.models import Ruta
from django.contrib.auth import logout
from.forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def principal(request):
    rutas_proximas = Ruta.objects.filter(
        status='activa',  
        fecha__gte=timezone.now().date()
    )
    return render(request, 'inicio/principal.html', {'rutas_proximas': rutas_proximas})

def exit(request):
    logout(request)
    return redirect('Principal')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                return redirect('Principal')
        else:
            messages.error(request, "El formulario no es válido. Por favor, revisa los datos ingresados.")

    return render(request, 'registration/register.html', data)


    