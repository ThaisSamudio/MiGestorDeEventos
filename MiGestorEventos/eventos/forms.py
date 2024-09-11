# forms.py
from django import forms
from .models import Evento, Organizador
from django.core.exceptions import ValidationError

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'fecha', 'organizador']

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if 'Cancelado' in titulo:
            raise ValidationError('El nombre del evento no puede contener la palabra "Cancelado".')
        return titulo

class OrganizadorForm(forms.ModelForm):
    class Meta:
        model = Organizador
        fields = ['nombre', 'email']

