from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path('detalle/', views.detalle, name='detalle'),
    path('admin/listar', views.ListarAdmin.as_view(), name='admin_listar'),
]