from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
	name=forms.CharField(max_length=200)
	user_email=forms.EmailField()
	user_phone=forms.CharField(max_length=13)
	subscription_type=forms.CharField(max_length=100)
	class Meta:
		model=User
		fields=("name","user_email","username","user_phone","subscription_type","password1","password2")

	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    self.fields['name'].widget.attrs.update({'placeholder':('Name')})
	    self.fields['username'].widget.attrs.update({'placeholder':('Username')})
	    self.fields['user_email'].widget.attrs.update({'placeholder':('Email')})
	    self.fields['user_phone'].widget.attrs.update({'placeholder':('Phone Number')})
	    self.fields['subscription_type'].widget.attrs.update({'placeholder':('Subscription Type')})
	    self.fields['password1'].widget.attrs.update({'placeholder':('Password')})        
	    self.fields['password2'].widget.attrs.update({'placeholder':('Repeat password')})

