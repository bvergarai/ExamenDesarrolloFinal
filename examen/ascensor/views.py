from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
# MENSAJES
from django.contrib import messages
# Importamos los modelos de los perros
from .models import OrdenTrabajo, RegistroCliente
# Importamos el Formulario

# Para redirigir las vistas
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


def inicio(request):
        # Se van agregar los post a la platilla.html
    ascensor = OrdenTrabajo.objects.filter(
        fecha__lte=timezone.now()).order_by('fecha')
    return render(request, 'ascensor/inicio.html',  {'ascensor': ascensor})


def redirigir(request):
    user = request.user
    ascensor = OrdenTrabajo.objects.filter(
        fecha__lte=timezone.now()).order_by('fecha')
       if user.('ascensor.admin'):
            return render(request, 'ascensor/inicio.html', {'ascensor': ascensor})
        else:
            return render(request, 'ascensor/inicio.html', {'ascensor': ascensor}) 


        def login(request):
        return render(request, 'iniciosesion/login.html', {})

        def redirigir(request):
