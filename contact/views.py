from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings    

from .forms import contactForm
import autoreply

# Create your views here.
def contact(request):
	"""about page"""
	title = "Contact"
	form = contactForm(request.POST or None) #form handling by view.
	
	if form.is_valid():
		user_name = form.cleaned_data['username']
		user_message = form.cleaned_data['message']
		emailsub = user_name + " tried contacting you on mDecommerce."
		emailFrom = form.cleaned_data['useremail']
		emailmessage = '%s %s user email: %s' %(user_message, user_name, emailFrom)
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(emailsub, emailmessage, emailFrom, emailTo, fail_silently=True)
		autoreply.autoreply(emailFrom)
	context = locals()
	template = 'contact.html' 
	return render(request,template,context)
 