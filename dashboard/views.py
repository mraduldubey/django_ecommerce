from django.shortcuts import render

# Create your views here.
def home(request):
	"""the homepage view"""
	context = locals()
	template = 'home.html'
	return render(request,template,context)

def about(request):
	"""about page"""
	context = locals()
	template = 'about.html'
	return render(request,template,context)

