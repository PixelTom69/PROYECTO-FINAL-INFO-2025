from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length=60)
	imagen = models.ImageField(upload_to = 'categorias', null = True)
	
	def __str__(self):
		return self.nombre
