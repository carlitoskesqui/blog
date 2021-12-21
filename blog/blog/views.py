from django.shortcuts import render
from apps.post.models import Post
from apps.secretos.models import Secretos

def inicio(request):	
	context = {
		"post": Post.objects.all(),
		"secretos": Secretos.objects.all()
	}

	return render(request, "inicio.html", context)

def login(request):	
	return render(request, "login.html")