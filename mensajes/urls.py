from django.urls import path
from mensajes import views

app_name = 'mensajes'

urlpatterns = [
    path('', views.VerMensajesView.as_view(), name='verMensajes'),
    path('crear/', views.crearMensaje, name='crearMensaje'),
    path('eliminar/<int:mensaje_id>/', views.EliminarMensaje.as_view(), name='eliminarMensaje'),
    path('usuario/', views.VerMensajesPorUsuarioView.as_view(), name='verMensajesUsuario'),  
]