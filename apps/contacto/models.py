from django.db import models
from django.utils import timezone

class Contacto(models.Model):
    nombre_completo = models.CharField(max_length=200, verbose_name="Nombre Completo")
    email = models.EmailField(verbose_name="Email")
    asunto = models.CharField(max_length=300, verbose_name="Asunto")
    mensaje = models.TextField(verbose_name="Mensaje")
    fecha_envio = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Envío")
    leido = models.BooleanField(default=False, verbose_name="Leído")
    
    class Meta:
        verbose_name = "Mensaje de Contacto"
        verbose_name_plural = "Mensajes de Contacto"
        ordering = ['-fecha_envio']
    
    def __str__(self):
        return f"{self.nombre_completo} - {self.asunto}"
