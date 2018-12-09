from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
# MENSAJES
from django.contrib import messages
# Importamos los modelos de los perros
from .models import OrdenTrabajo, RegistroCliente
# Importamos el Formulario
from .forms import RegistroCliente_form, OrdenTrabajo_form
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
    elevador = OrdenTrabajo.object.order_by('fecha')
    if user.has_perm('ascensor.admin'):
        return render(request, 'ascensor/inicio.html', {'elevador': elevador})
    else:
        return render(request, 'ascensor/inicio.html', {'elevador': elevador})


def login(request):
        return render(request, 'iniciosesion/login.html', {})


def agregarclientes(request):
    admin = RegistroCliente.objects.order_by('Nombre_Completo')
    return render(request, 'ascensor/agregarcliente.html', {'admin': admin})


#AGREGAR CLIENTES
def agregarclientes(request):
   if request.method == "POST":
       form = RegistroCliente_form(request.POST or None, request.FILES or None)
       if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.fecha_publicacion = timezone.now()
           post.save()
           messages.info(request, 'El Cliente se agrego correctamente!')
           return redirect('adm.inicio')
   else:
       form = RegistroCliente_form()
   return render(request, 'ascensor/administrador.html', {'form': form})

   #Vista para ventana de ficha
   def crearficha(request):
    orden = OrdenTrabajo.objects.order_by('fecha')
    return render(request, 'ascensor/ordentrabajo.html', {'orden': orden})


   #Crear Ficha
def crearficha(request):
   if request.method == "POST":
       form = OrdenTrabajo_form(request.POST or None, request.FILES or None)
       if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.fecha = timezone.now()
           post.save()
           messages.info(request, 'El Formulario se Creo Correctamente')
           return redirect('paginaprincipal')
   else:
       form = OrdenTrabajo_form()
   return render(request, 'ascensor/ordentrabajo.html', {'form': form})

   #vista de clientes disponibles
def verClientes(request):
    clientes = RegistroCliente.objects.all()
    return render(request, 'ascensor/clientes.html',  {'clientes': clientes})
