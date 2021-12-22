from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length=255)

	class Meta:
		db_table="categorias"

	def __str__(self):
		return self.nombre
	

class Post(models.Model):
	titulo = models.CharField(max_length=250)
	cuerpo = models.CharField(max_length=250)
	fecha_creacion = models.TimeField(auto_now_add=True)
	autor= models.CharField(max_length=100)
	thumbnail = models.ImageField()
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)

	class Meta:
		db_table="post"

	def __str__(self):
		return self.nombre


