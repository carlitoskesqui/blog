from django import forms
from django.forms import fields
from .models import Post


class PostForm(forms.ModelForm):
	titulo = forms.CharField(label="Título", widget=forms.TextInput(attrs={"class":"form-control"}))
	cuerpo = forms.CharField(label="Contenido", widget=forms.Textarea(attrs={'class':'form-control', 'rows': 5, 'cols': 100}))
	#categorias
	imagen=forms.ImageField(label="Subir Imagen")
	class Meta:
		model = Post
		fields = ["titulo", "cuerpo", "imagen"]








"""
from django 	import forms
from .models 	import Post


class PostForm(forms.ModelForm):
	titulo = forms.CharField(label="Título", widget=forms.TextInput(attrs={"class":"form-control"}))
	cuerpo = forms.CharField(label="Contenido", widget=forms.Textarea(attrs={'class':'form-control', 'rows': 5, 'cols': 100}))

	class Meta:
		model = Post
		fields = ["titulo", "cuerpo"]

"""