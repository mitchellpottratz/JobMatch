from functools import wraps
from django.http import HttpResponseRedirect


# this decorators checks if the current user is a company_user, and redirects
# them to the login user if they are not a company_user
def company_account_required(function):
	@wraps(function)
	def wrap(request, *args, **kwargs):
		if not request.user.company_user:
			return HttpResponseRedirect('/users/login/')
		else:
			return function(request, *args, **kwargs)
	return wrap



