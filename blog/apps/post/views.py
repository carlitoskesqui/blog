from django.shortcuts 		import render
from django.views.generic 	import ListView, CreateView
from .models 				import Post
from .forms 				import PostForm
from django.urls 			import reverse_lazy

def detalle(request):	
	context = {}
	return render(request, "post/detalle.html", context)

class ListarAdmin(ListView):
	template_name="post/admin/listar.html"
	model = Post
	context_object_name="post"

	"""
	Filtrar lista:
	def get_queryset(self):
		return Post.objects.filter(id=2)
	"""

class NuevoPost(CreateView):
	template_name = "post/admin/nuevo.html"
	model = Post
	form_class = PostForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("post:admin_listar")