from django.urls import path
from . import views 

app_name = "articulos"
urlpatterns = [
    path('Listar/', views.Listar_Articulos, name="path_listar_articulos"),
    path('Detalle/<int:pk>/', views.detalle_articulo, name='path_detalle_articulo'),
    path('Crear/', views.Crear_Articulo.as_view(), name='path_crear_articulo'),
    path('Modificar/<int:pk>/', views.Modificar_Articulo.as_view(), name='path_modificar_articulo'),
    path('Eliminar/<int:pk>/', views.Borrar_Articulo.as_view(), name='path_borrar_articulo'),

    #filtro por rubro
    path("filtrados/<int:pk>", views.Filtrar_Categoria , name="path_filtro_categoria")

]
