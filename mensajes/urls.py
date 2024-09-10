from django.urls import path
from . import views

nombreAplicacion = 'mensajes'

urlpatterns = [
    path('mensajes/<str:tipo>/', views.verMensajes, name='verMensajes'),
    path('crear/', views.crearMensaje, name='crearMensaje'),
    path('eliminar/<int:mensaje_id>/', views.eliminarMensaje, name='eliminarMensaje'),
]
