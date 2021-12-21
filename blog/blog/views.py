from django.shortcuts import render
from apps.post.models import Post

def inicio(request):	
	post = Post.objects.all()

	usuario = {
		"nombre": "Carlos",
		"apellido": "Kesqui"
	}

	context = {
		"usuario": usuario,
		"post": post
	}

	return render(request, "inicio.html", context)