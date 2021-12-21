from django.db import models


class Post(models.Model):
	titulo = models.CharField(max_length=250)
	cuerpo = models.CharField(max_length=250)
	fecha_creacion = models.CharField(max_length=30)
	autor= models.CharField(max_length=100)
	#geeks_field = models.TimeField()
	#foto = models.ImageField()

	class Meta:
		db_table="post"
