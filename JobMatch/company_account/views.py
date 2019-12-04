from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# import decorator that checks if current user is a company user
from .decorators import company_account_required


# this view is where a company user can view all
# of their information
@login_required
@company_account_required
def index(request):
	# gets the current user
	user = request.user

	# gets the users company
	company = request.user.company_account

	# data being passed into the template
	context = {
		'user': user,
		'company': company
	}
	return render(request, 'company_account/index.html', context)


