from django.db import models
from genericos.models import Categoria

class Articulo(models.Model):
    creado = models.DateTimeField(
        auto_now_add=True
    )
    modificado = models.DateTimeField(
        auto_now=True
    )
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    resumen = models.TextField(max_length=300, help_text="Breve descripción del artículo")
    imagen_destacada = models.ImageField(upload_to='articulos', blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, help_text="Separar con comas")
    categoria= models.ForeignKey(Categoria, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo

    def misComentarios(self):
        return self.comentario_set.all()    


    # MIGRACIONES
# PASOS
# 1 - verificar que cambios existen
	# python manage.py makemigrations
# 2 - aplicar los cambios
	# python manage.py migrate
