from django.shortcuts import render

def detalle(request):	
	context = {
		#"post": Post.objects.all(),
		#"secretos": Secretos.objects.all()
	}
	return render(request, "post/detalle.html", context)