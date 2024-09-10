from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.decorators import login_required


class VerMensajesView(View):
    def get(self,request):
        mensajes = Mensaje.objects.all()
        return render(request,'mensajes/verMensajes.html',{'mensajes':mensajes})
    

def verMensajes(request, tipo):
    if tipo == 'recibidos':
        mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha_envio')
    elif tipo == 'enviados':
        mensajes = Mensaje.objects.filter(remitente=request.user).order_by('-fecha_envio')
    else:
        mensajes = []
    return render(request, 'mensajes.html', {'mensajes': mensajes, 'tipo': tipo})


def crearMensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.save()
            return redirect('mensajes:verMensajes')
    else:
        form = MensajeForm()
    return render(request, 'mensajes/crearMensajes.html', {'form': form})


class VerMensajesPorUsuarioView(View):
    def get(self,request):
        usuario = request.GET.get('usuario',None)

        if usuario:
            mensajes_recibidos = Mensaje.objects.filter(destinatario__icontains=usuario)
            mensajes_enviados = Mensaje.objects.filter(remitente__icontains=usuario)

        else:
            return render(request, 'mensajes/verMensajesUsuario.html',{'mensajes_enviados':[],'mensajes_recibidos':[]})
        
        return render(request, 'mensajes/verMensajesUsuario.html',{'mensajes_enviados':mensajes_enviados,'mensajes_recibidos':mensajes_recibidos})
        


class EliminarMensaje(View):
    def post(self, request, mensaje_id):
        mensaje = get_object_or_404(Mensaje, pk=mensaje_id)
        mensaje.delete() 
        return redirect('mensajes:verMensajes') 