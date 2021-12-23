from django.core.exceptions import PermissionDenied
class AdminRM():
	

	def dispatch(self, request, *args, **kwars):

		if not request.user.administrador:
			raise PermissionDenied
		return super(AdminRM, self).dispatch(request, *args, **kwars)