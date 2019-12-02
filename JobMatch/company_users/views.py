from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from users.models import User
from .models import Company
from .forms import CompanyForm
from .invite_code import generate_invite_code


# this view is where registered company users can join 
# a company by using the companies invite code
def join(request):

	# if the form was submitted
	if request.method == 'POST':

		# gets the invite code from the form
		code = request.POST.get('code')

		try:
			company = Company.objects.get(invite_code=code)
		except Company.DoesNotExists:
			print('company code does not exist')

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



