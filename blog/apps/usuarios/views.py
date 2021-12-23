from django.shortcuts 			import render
from django.views.generic 		import ListView, CreateView, DeleteView, DetailView
from django.views.generic.edit 	import UpdateView
from .models 					import Usuarios
from .forms 					import UsuariosForm
from django.urls 				import reverse_lazy

class NuevoUsuario(CreateView):
	template_name = "usuarios/registrarse.html"
	model = Usuarios
	form_class = UsuariosForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("login")