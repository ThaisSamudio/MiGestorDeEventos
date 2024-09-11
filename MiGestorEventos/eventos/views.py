from django.shortcuts import render, redirect 
from .models import Evento
from .forms import EventoForm
from  . import forms
from django.views.generic import ListView, CreateView
from .models import Organizador
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

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

