from django import forms
from django.forms import fields
from django.contrib.auth.forms import UserCreationForm
from .models import Usuarios



class UsuariosForm(UserCreationForm):
	username = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Usuario"}))
	password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Contraseña"}))
	first_name = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Nombres"}))
	last_name = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Apellido"}))
	email = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Correo Electrónico"}))

	class Meta:
		model = Usuarios
		fields = ["username", "first_name", "last_name", "email"]