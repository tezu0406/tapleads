from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
	Name=forms.CharField(max_length=200)
	User_Email=forms.EmailField()
	Subscription_type=forms.CharField(max_length=200)
	class Meta:
		model=User
		fields=("Name","User_Email","username","Subscription_type","password1","password2")
