from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, Organizador
from .forms import EventoForm
from django.views.generic import ListView, CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout

def eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'evento.list.html', {'eventos': eventos})


def crearEventos(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evento-list')  # Redirige a una vista específica después de guardar
    else:
        form = EventoForm()

    return render(request, 'evento_form.html', {'form': form})

class OrganizadorListView(ListView):
    model = Organizador
    template_name = 'organizador_list.html'
    context_object_name = 'organizadores'

class OrganizadorCreateView(CreateView):
   model = Organizador
   fields = '__all__'
   success_url = '/organizadores/'
   template_name = 'organizador_form.html'
   success_message = 'Organizador creado correctamente.'


def iniciarSesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('evento-list')  # Redirigir a la lista de eventos después del login
        else:
            messages.error(request, 'Credenciales incorrectas. Inténtalo nuevamente.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


@login_required
def editar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, 'El evento ha sido actualizado.')
            return redirect('evento-list')
    else:
        form = EventoForm(instance=evento)

    return render(request, 'editar_evento.html', {'form': form, 'evento': evento})


def registrarse(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Autentica y logea al usuario después del registro
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
            return redirect('login')  # Redirige al usuario a la página principal
    else:
        form = UserCreationForm()
    
    return render(request, 'registrarse.html', {'form': form})

def cerrarSesion(request):
    logout(request)
    return redirect('evento-list') 