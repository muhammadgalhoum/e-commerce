from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from.models import Profile


class UserRegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['name', 'gender', 'profile_pic']


class UserDeleteForm(forms.ModelForm):
	class Meta:
		model = User
		fields = []  # Form has only submit button. Empty list still necessary.