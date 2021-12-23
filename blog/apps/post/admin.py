from django.contrib import admin

from .models import Post, Categorias

admin.site.register(Categorias)
admin.site.register(Post)

