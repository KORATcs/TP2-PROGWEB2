from django.db import models
from django.utils import timezone

# Create your models here.

class Mensaje (models.Model):
    texto = models.TextField()
    remitente = models.CharField(max_length=1000)
    destinatario = models.CharField(max_length=1000)
    fecha_hora_envio = models.DateTimeField(default=timezone.now)