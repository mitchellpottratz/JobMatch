from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


# form for registering new users
class RegisterForm(UserCreationForm):

	# adds a widget, css class and placeholder to each form field
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
	company_user = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
	candidate_user = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

	class Meta(UserCreationForm.Meta):
 		model = User

 		# all of the fields that are included in the form
 		fields = (
 			'first_name',
 			'last_name',
 			'email',
 			'username',
 			'password1',
 			'password2'
 		)

 	# forms save method - creates a new user
	def save(self, commit=True):

 		# create new user and save it
		user = User(username=self.cleaned_data['username'],
					first_name=self.cleaned_data['first_name'],
					last_name=self.cleaned_data['last_name'],
					email=self.cleaned_data['email'],
					company_user=self.cleaned_data['company_user'],
					candidate_user=self.cleaned_data['candidate_user'])
		user.save()

        # sets the users password
		user.set_password(self.cleaned_data["password1"])
        
        # saves the user again and returns it
		if commit:
			user.save()
		return user




 