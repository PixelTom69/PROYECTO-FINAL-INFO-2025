from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views # Clase del 3-7-25

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="path_home"),
   
    # Incluir las apps CON namespaces
    path("Articulos/", include("articulos.urls", namespace="articulos")),
    path("Genericos/", include("genericos.urls", namespace="genericos")),
    path('Usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('Comentarios/', include('comentarios.urls', namespace='comentarios')),
    path('contacto/', include('contacto.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
