from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('eventos/', views.eventos, name='evento-list'),
    path('crearEvento/', views.crearEventos, name='evento_form'),
    path('organizadores/', views.OrganizadorListView.as_view(), name='organizador-list'),
    path('organizadores/crear/', views.OrganizadorCreateView.as_view(), name='organizador-crear'),
    path('login/', views.iniciarSesion, name='login'),
    path('editar-evento/<int:id>/', views.editar_evento, name='editar-evento'),
    path('registrarse/',views.registrarse, name='registrarse'),
    path('logout/', views.cerrarSesion, name='logout'),
    
]

