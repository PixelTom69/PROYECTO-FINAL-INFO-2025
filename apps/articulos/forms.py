from django import forms
from .models import Articulo

class FormularioCrearArticulo(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ("titulo", "contenido", "resumen", "imagen_destacada", "categoria")

class FormularioModificarArticulo(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ("titulo", "contenido", "resumen", "imagen_destacada", "categoria")