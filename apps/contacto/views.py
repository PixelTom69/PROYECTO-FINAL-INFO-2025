from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactoForm
from .models import Contacto

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Mensaje enviado exitosamente! Te contactaremos pronto.')
            return redirect('contacto:contacto')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = ContactoForm()
    
    context = {
        'form': form
    }
    return render(request, 'contacto/contacto.html', context)

def listar_contactos(request):
    """Vista para listar todos los contactos (opcional, para staff)"""
    contactos = Contacto.objects.all().order_by('-fecha_envio')
    context = {
        'contactos': contactos
    }
    return render(request, 'contacto/listar.html', context)
