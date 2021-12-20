from django.shortcuts import render

def inicio(request):	
	post = [
		{"nombre": "Post 1", "cuerpo": "Este es el cuerpo 1"},
		{"nombre": "Post 2", "cuerpo": "Este es el cuerpo 2"},
		
	]

	usuario = {
		"nombre": "Carlos",
		"apellido": "Kesqui"
	}

	context = {
		"usuario": usuario,
		"post": post
	}

	return render(request, "inicio.html", context)