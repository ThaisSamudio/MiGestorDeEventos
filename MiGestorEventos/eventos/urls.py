from django.urls import path
from . import views

urlpatterns = [
    path('eventos/', views.eventos, name='evento-list'),
    path('crearEvento/', views.crearEventos, name='evento_form'),

]
