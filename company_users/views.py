
# django imports 
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# model imports
from users.models import User
from .models import Company

# form imports 
from .forms import CompanyForm

# imports function that generates a companies invite code
from .invite_code import generate_invite_code

# imports decorator that checks if the current user is apart of a company
from .decorators import no_company


# this view is where registered company users can join 
# a company by using the companies invite code
@login_required
@no_company
def join(request):

	# if the form was submitted
	if request.method == 'POST':

		# gets the invite code from the form
		code = request.POST.get('code')

		try:
			# gets the company by the invite code from the form
			company = Company.objects.get(invite_code=code)

			# adds the current user to whatever company the invite 
			# code was for
			user = request.user
			user.company_account = company
			user.save()

			return redirect('/company-account/index')

		# if the invite code does not exist 	
		except ObjectDoesNotExist:
			
			# creates error message to show to the user
			messages.error(request, 'The invite code you entered does not exist')

	return render(request, 'company_users/join.html')


# this view is where registered company users can create 
# a new company
@login_required
@no_company
def create_company(request):
	# gets the current user
	user = request.user

	# if the form was submitted
	if request.method == 'POST':

		# creates a new form instance passing in the data
		form = CompanyForm(request.POST, request.FILES)

		# if the form is valid
		if form.is_valid():
			company = form.save(commit=False)
			company.admin = user # the user that created th company becomes the admin
			company.invite_code = generate_invite_code() # generates random invite code string
			company.save()

			# adds the company to the users company_account field
			user.company_account = company 
			user.save()
			return redirect('/company-account/')

	# if the https method is GET
	else:
		# creates a form instance with no data
		form = CompanyForm() 
		
	return render(request, 'company_users/create_company.html', {'form': form})


def new_company(request):
	return HttpResponse('company created')



