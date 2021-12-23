from django.urls                import path
from .                          import views

app_name = "usuarios"

urlpatterns = [
    path('registrarse/', views.NuevoUsuario.as_view(), name='registrarse'),
] 