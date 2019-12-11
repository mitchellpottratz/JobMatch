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
	company = user.company_account

	# gets all of the companies users excluding the current user
	company_users = company.users.all().exclude(id=user.id)

	# if the current user is the admin
	if company.admin == user:
		is_admin = True
	else:
		is_admin = False

	# data being passed into the template
	context = {
		'user': user,
		'company': company,
		'company_users': company_users, 
		'is_admin': is_admin,
		'nav': 'account'
	}
	return render(request, 'company_account/index.html', context)






