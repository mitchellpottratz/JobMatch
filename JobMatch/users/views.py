
# django imports
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# model imports 
from users.models import User
from company_users.models import Company

# form imports 
from .forms import RegisterForm


# this view is where people register for a CompanyUser account
def register(request):

	# if the registration form was submitted
	if request.method == 'POST':
		print('method is post')

		# pass the form data to the RegisterForm
		form = RegisterForm(request.POST)

		# if the form is valid
		if form.is_valid():
	
			# creates the user
			form.save()

			# authenticates the user and logs them in
			user = authenticate(
				username=form.cleaned_data.get('username'),
				password=form.cleaned_data.get('password1')
			)
			auth_login(request, user)

			# if the user is a company user
			if user.company_user:
				# take them to the page where they can join their company
				return redirect('/company-users/join/')

			# if the user is a candidate user 
			else:
				# take them to the page where they fill out the 
				# rest of their account information
				return redirect('/candidate-users/complete-info/')
		else:
			print(form.errors)

	# if the form was not submitted
	else:
		form = RegisterForm()

	return render(request, 'users/register.html', {'form': form})


# this is where candidate or company users login
def login(request):

	# if the form was submitted
	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']

		# authenticates the user with the username and password
		# from the form
		user = authenticate(
			username=username,
			password=password
		)

		# if the user exists
		if user is not None:
			# logs in the user
			auth_login(request, user)

			# if the user is a company_user
			if user.company_user:
				return redirect('/company-users/join/')

			# if the user is a candidate user
			else:
				return redirect('/candidate-users/complete-info/')

		# if the user does not exist
		else:
			# creates error message to show the client
			messages.error(request, 'The username or password is incorrect')

	return render(request, 'users/login.html')















