from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Evento

class EventoListView(ListView):
    model = Evento
    template_name = 'eventos/evento_list.html'
    context_object_name = 'eventos'


from django.views.generic.edit import CreateView
from .models import Evento
from .forms import EventoForm

class EventoCreateView(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/evento_form.html'
    success_url = '/eventos/'
