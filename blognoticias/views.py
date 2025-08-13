from django.shortcuts import render
from django.apps import apps  # Importación más segura

def home(request):
    # Obtener los últimos 6 artículos para mostrar en home
    try:
        # Importación dinámica para evitar problemas circulares
        Articulo = apps.get_model('articulos', 'Articulo')
        articulos_destacados = Articulo.objects.all().order_by('-creado')[:6]
    except:
        # Si hay algún error, usar lista vacía (se mostrarán las noticias estáticas)
        articulos_destacados = []
    
    context = {
        'articulos_destacados': articulos_destacados
    }
    return render(request, 'home.html', context)