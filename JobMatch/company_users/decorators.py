from functools import wraps
from django.http import HttpResponseRedirect


# this decorator checks if the current user is apart of a company
def no_company(function):
	@wraps(function)
	def wrap(request, *args, **kwargs):
		user = request.user
		if user.company_account:
			return HttpResponseRedirect('/company-account/index')
		else:
			return function(request, *args, **kwargs)
	return wrap




