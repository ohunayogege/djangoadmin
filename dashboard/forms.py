from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm


class DeactivateProfileForm(ModelForm):
	class Meta:
		model = User
		fields = (
			'email',
			'first_name',
			'last_name'
		)
class ProfileForm(ModelForm):
	class Meta:
		model = User
		fields = ('is_active',) #Note that we didn't mention user field here.
