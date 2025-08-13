from django.urls import path
from . import views 

app_name = "genericos"

urlpatterns = [
   path("Categorias/", views.Listar_Categorias, name="path_listar_categorias"),
   path("acerca-de/", views.acerca_de, name="acerca_de"),  # ← NUEVA URL
]