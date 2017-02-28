from django.shortcuts import render

# Create your views here.
def home(request):
	"""the homepage view"""
	context = {}
	template = 'home.html'
	return render(request,template,context)

def about(request):
	"""about page"""
	context = {}
	template = 'about.html'
	return render(request,template,context)

