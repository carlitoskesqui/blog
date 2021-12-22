from django.urls    import path
from .              import views

app_name = "post"

urlpatterns = [
    path('detalle/', views.detalle, name='detalle'),

    # Usuario Registrado
    path('admin/listar', views.ListarAdmin.as_view(), name='admin_listar'),
    path('admin/nuevo', views.NuevoPost.as_view(), name='admin_nuevo'),
    path('admin/editar/<int:pk>/', views.EditarPost.as_view(), name='admin_editar'),
]