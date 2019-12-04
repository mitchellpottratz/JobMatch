from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# import decorator that checks if current user is a company user
from .decorators import company_account_required


# this view is where a company user can view all
# of their information
@login_required
@company_account_required
def index(request):
	return render(request, 'index.html')


