from django.urls import path
from . import views


urlpatterns = [
    path('eventos/', views.eventos, name='evento-list'),
    path('crearEvento/', views.crearEventos, name='evento_form'),
    path('organizadores/', views.OrganizadorListView.as_view(), name='organizador-list'),
    path('organizadores/crear/', views.OrganizadorCreateView.as_view(), name='organizador-crear'),
    

]
