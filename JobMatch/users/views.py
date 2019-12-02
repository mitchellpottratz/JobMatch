from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from users.models import User
from company_users.models import Company
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
			login(request, user)

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

	return render(request, 'register.html', {'form': form})





