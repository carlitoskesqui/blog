from django.shortcuts 		import render
from django.views.generic 	import ListView
from .models 				import Post

def detalle(request):	
	context = {}
	return render(request, "post/detalle.html", context)

class ListarAdmin(ListView):
	template_name="post/admin/listar.html"
	model = Post
	context_object_name="post"