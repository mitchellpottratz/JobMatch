from django.shortcuts import render
from django.http import HttpResponse

# this is where the user fills out the rest of their information
# after they register
def complete_info(request):
	return HttpResponse('candidate info page')







