from django import forms

class contactForm(forms.Form): #new form called contactForm
 	username = forms.CharField(required=True,max_length=50,help_text='limit 50 chars')
	useremail = forms.EmailField(required=True)
	message = forms.CharField(required=True,widget=forms.Textarea) 
	#This widget overrides the defualt widdget defult in CharField. See Dj Docs.
