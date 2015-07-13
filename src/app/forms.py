from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model  = SignUp
		fields = ['full_name','email']
		#exclude = ['full_name']
	def clean_email(self):
		#print self.cleaned_data # python 2.7
		email = (self.cleaned_data.get('email')) #python 3.X
		email_base , provider = email.split("@")
		domain , extension = provider.split('.')
		if not domain == 'USC':
			raise forms.ValidationError("Please make sure you use your USC email")
		if not extension=="edu":
			raise forms.ValidationError("Plesae use a valid .EDU email address")
		return email

	def  clean_full_name(self):
			full_name = self.cleaned_data.get('full_name')
			return full_name	
		#return "abc@hotmail.com"


	#def clean_fullname(self):
	#	print (self.cleaned_data)