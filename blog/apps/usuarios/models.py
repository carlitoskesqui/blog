from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuarios(AbstractUser):
	dni= models.IntegerField(null=True, blank=True)
	#foto = models.ImageField()

	class Meta:
		db_table="usuarios"

	def __str__(self):
		return self.get_full_name()
