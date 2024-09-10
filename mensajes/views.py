from django.shortcuts import render, get_object_or_404, redirect
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.decorators import login_required

@login_required
def verMensajes(request, tipo):
    if tipo == 'recibidos':
        mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha_envio')
    elif tipo == 'enviados':
        mensajes = Mensaje.objects.filter(remitente=request.user).order_by('-fecha_envio')
    else:
        mensajes = []
    return render(request, 'mensajes.html', {'mensajes': mensajes, 'tipo': tipo})

@login_required
def crearMensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect('ver_mensajes', tipo='enviados')
    else:
        form = MensajeForm()
    return render(request, 'crear_mensaje.html', {'form': form})

@login_required
def eliminarMensaje(request, mensaje_id):
    mensaje = get_object_or_404(Mensaje, id=mensaje_id, remitente=request.user)
    if request.method == 'POST':
        mensaje.delete()
        return redirect('ver_mensajes', tipo='enviados')
    return render(request, 'eliminar_mensaje.html', {'mensaje': mensaje})
