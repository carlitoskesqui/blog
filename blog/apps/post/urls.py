from django.urls    import path
from .              import views

app_name = "post"

urlpatterns = [
    path('detalle/', views.detalle, name='detalle'),

    # Usuario Registrado
    path('admin/listar', views.ListarAdmin.as_view(), name='admin_listar'),
    path('admin/nuevo', views.NuevoPost.as_view(), name='admin_nuevo'),
    path('admin/editar/<int:pk>/', views.EditarPost.as_view(), name='admin_editar'),
    path('admin/eliminar/<int:pk>/', views.EliminarPost.as_view(), name='admin_eliminar'),
    path('admin/ver/<int:pk>/', views.VerPost.as_view(), name='admin_ver'),
]