from django.db import models

class Post(models.Model):
	titulo = models.Charfield(max_length=250)
	cuerpo = models.Charfield(max_length=250)
	fecha_creacion = models.Charfield(max_length=30)
	autor= models.Charfield(max_length=100)
