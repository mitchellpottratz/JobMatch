
# django imports 
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# model imports
from users.models import User
from .models import Company

# form imports 
from .forms import CompanyForm

# imports function that generates a companies invite code
from .invite_code import generate_invite_code


# this view is where registered company users can join 
# a company by using the companies invite code
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

			return redirect('/success/')

		# if the invite code does not exist 	
		except ObjectDoesNotExist:
			print('company code does not exist')

			# creates error message to show to the user
			messages.error(request, 'The invite code you entered does not exist')

	return render(request, 'join.html')


# this view is where registered company users can create 
# a new company
def create_company(request):

	# if the form was submitted
	if request.method == 'POST':

		# creates a new form instance passing in the data
		form = CompanyForm(request.POST, request.FILES)

		# if the form is valid
		if form.is_valid():
			company = form.save(commit=False)
			company.admin = request.user # the user that created th company becomes the admin
			company.invite_code = generate_invite_code() # generates random invite code string
			company.save()
			return redirect('/company-users/company')

	# if the https method is GET
	else:
		# creates a form instance with no data
		form = CompanyForm() 
		
	return render(request, 'create_company.html', {'form': form})


def new_company(request):
	return HttpResponse('company created')



