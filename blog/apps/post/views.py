from django.shortcuts 			import render
from django.views.generic 		import ListView, CreateView, DeleteView, DetailView
from django.views.generic.edit 	import UpdateView
from .models 					import Post
from .forms 					import PostForm
from django.urls 				import reverse_lazy

def detalle(request):	
	context = {}
	return render(request, "post/detalle.html", context)

class ListarAdmin(ListView):
	template_name="post/admin/listar.html"
	model = Post
	context_object_name="post"
	
	def get_queryset(self):
		return Post.objects.all().order_by("fecha_creacion")
	

class NuevoPost(CreateView):
	template_name = "post/admin/nuevo.html"
	model = Post
	form_class = PostForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("post:admin_listar")


class EditarPost(UpdateView):
	template_name = "post/admin/editar.html"
	model = Post
	form_class = PostForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("post:admin_listar")


class EliminarPost(DeleteView):
	template_name = "post/admin/eliminar.html"
	model = Post

	def get_success_url(self, **kwargs):
		return reverse_lazy("post:admin_listar")



class VerPost(DetailView):
	template_name = "post/admin/ver.html"
	model = Post

	def get_success_url(self, **kwargs):
		return reverse_lazy("post:admin_listar")