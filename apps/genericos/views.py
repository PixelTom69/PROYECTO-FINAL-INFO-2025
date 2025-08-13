from django.shortcuts import render
from .models import Categoria

def Listar_Categorias(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
        'articulos': [],  # Lista vacía temporal
    }
    return render(request,"genericos/categorias.html", context)

def acerca_de(request):
    context = {
        'integrantes': [
            {
                'nombre': 'Tu Nombre',
                'rol': 'Full Stack Developer',
                'descripcion': 'Especializado en desarrollo web con Django y tecnologías frontend modernas.',
                'github': 'https://github.com/tu-usuario',
                'linkedin': 'https://linkedin.com/in/tu-perfil',
                'avatar': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&h=300&fit=crop&crop=face'
            },
            {
                'nombre': 'Segundo Integrante',
                'rol': 'Frontend Developer', 
                'descripcion': 'Experto en diseño de interfaces y experiencia de usuario.',
                'github': 'https://github.com/usuario2',
                'linkedin': 'https://linkedin.com/in/perfil2',
                'avatar': 'https://images.unsplash.com/photo-1494790108755-2616b612b647?w=300&h=300&fit=crop&crop=face'
            },
            {
                'nombre': 'Tercer Integrante',
                'rol': 'Backend Developer',
                'descripcion': 'Especializado en desarrollo backend y bases de datos.',
                'github': 'https://github.com/usuario3',
                'linkedin': 'https://linkedin.com/in/perfil3',
                'avatar': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=300&h=300&fit=crop&crop=face'
            }
        ],
        'proyecto_info': {
            'nombre': 'Turismo Chaco',
            'descripcion': 'Plataforma web dedicada a promover el turismo en la provincia del Chaco, Argentina. Desarrollada con Django y tecnologías web modernas.',
            'tecnologias': ['Django', 'Python', 'HTML5', 'CSS3', 'JavaScript', 'SQLite', 'Bootstrap'],
            'año': '2025'
        }
    }
    return render(request, 'genericos/acerca_de.html', context)