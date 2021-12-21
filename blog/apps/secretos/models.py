from django.db import models

class Secretos(models.Model):
	titulo = models.CharField(max_length=250)
	cuerpo = models.CharField(max_length=250)
	fecha_creacion = models.CharField(max_length=30)
	autor= models.CharField(max_length=100)
	#foto = models.ImageField()

	class Meta:
		db_table="secretos"
