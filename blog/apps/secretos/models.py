from django.db import models

class Secretos(models.Model):
	titulo_s = models.CharField(max_length=250)
	cuerpo_s = models.CharField(max_length=250)
	fecha_creacion_s = models.CharField(max_length=30)
	autor_s = models.CharField(max_length=100)
	#foto = models.ImageField()

	class Meta:
		db_table="secretos"
