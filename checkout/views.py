from django.contrib.auth.decorators import login_required #the login_required decorator
from django.shortcuts import render
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.
@login_required
def checkout(request):
	'''checkout view function'''
	publishkey = settings.STRIPE_PUBLISHABLE_KEY
	if request.method == 'POST':
		print request.POST['stripeToken']
		token = request.POST['stripeToken']
		#Charge the user's card:
		try:
			charge = stripe.Charge.create(
			  amount=1000,
			  currency="usd",
			  description="Example charge",
			  source=token,
			) 
		except stripe.error.CardError as e:
			print 'The Card has been declined'
			pass
	context = {'publishKey':publishkey }
	template = 'checkout.html'
	return render(request,template,context)
