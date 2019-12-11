from functools import wraps
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import CandidateInfo



# this decorator checks if the current user has filled out their
# candidate info yet
def no_candidate_info(function):
	@wraps(function)
	def wrap(request, *args, **kwargs):
		if CandidateInfo.objects.filter(user=request.user):
			return HttpResponseRedirect('/candidate-account/')
		else:
			return function(request, *args, **kwargs)
	return wrap





