from django.urls import path
from . import views

#INDICO COMO SE LLAMA LA APP
app_name = "comentarios"

urlpatterns = [
    path('Agregar/<int:pk>', views.Comentar, name = "path_comentar"),
    path('Eliminar/<int:pk>', views.Eliminar.as_view(), name = "path_eliminar_comentario")
]