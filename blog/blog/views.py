from django.shortcuts import render
from apps.post.models import Post
from django.views.generic.base import TemplateView

"""
def inicio(request):	
	context = {
		"post": Post.objects.all(),
		"secretos": Secretos.objects.all()
	}

	return render(request, "inicio.html", context)
"""

#def login(request):	
#	return render(request, "login.html")

class Inicio(TemplateView):
	template_name = "inicio.html"

	def get_context_data(self, **kwargs):
		context = super(Inicio, self).get_context_data(**kwargs)
		context["post"] = Post.objects.all()
		return context
