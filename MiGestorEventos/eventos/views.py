from django.shortcuts import render, redirect 
from .models import Evento
from .forms import EventoForm
from  . import forms

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