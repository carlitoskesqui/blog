from django.contrib.auth.mixins	import LoginRequiredMixin
from django.shortcuts 			import render
from django.views.generic 		import ListView, CreateView, DeleteView, DetailView
from django.views.generic.edit 	import UpdateView
from .models 					import Post
from .forms 					import PostForm
from django.urls 				import reverse_lazy
from apps.core.mixins			import AdminRM

class ListarAdmin(LoginRequiredMixin,  ListView):
	template_name="post/admin/listar.html"
	model = Post
	context_object_name="post"
	paginate_by = 6

	def get_context_data(self, **kwargs):
		context = super(ListarAdmin, self).get_context_data(**kwargs)
		context["buscado"] = self.request.GET.get("nombre_post", "")
		return context
	
	def get_queryset(self):
		busqueda_nombre = self.request.GET.get("nombre_post", "")
		query = Post.objects.all().order_by("titulo")
		if len(busqueda_nombre) > 0:
			query = query.filter(titulo__icontains=busqueda_nombre)
		return query
	

class NuevoPost(LoginRequiredMixin,  CreateView):
	template_name = "post/admin/nuevo.html"
	model = Post
	form_class = PostForm


	def get_success_url(self, **kwargs):
		return reverse_lazy("post:admin_listar")


class EditarPost(LoginRequiredMixin,  UpdateView):
	template_name = "post/admin/editar.html"
	model = Post
	form_class = PostForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("post:admin_listar")


class EliminarPost(LoginRequiredMixin,  DeleteView):
	template_name = "post/admin/eliminar.html"
	model = Post
	

	def get_success_url(self, **kwargs):
		return reverse_lazy("post:admin_listar")



class VerPost(DetailView):
	template_name = "post/admin/ver.html"
	model = Post

	def get_success_url(self, **kwargs):
		return reverse_lazy("post:admin_listar")


class Detalle(DetailView):
	template_name = "post/detalle.html"
	model = Post

	def get_context_data(self, **kwargs):
		context = super(Detalle, self).get_context_data(**kwargs)
		context["buscado"] = self.request.GET.get("nombre_post", "")
		return context
	
	def get_queryset(self):
		busqueda_nombre = self.request.GET.get("nombre_post", "")
		query = Post.objects.all().order_by("titulo")
		if len(busqueda_nombre) > 0:
			query = query.filter(titulo__icontains=busqueda_nombre)
		return query	