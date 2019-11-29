from django.shortcuts import render
from users.models import User
from .models import Company


# this view is where people register for a CompanyUser account
def register(request):
	return HttpResponse('company users working')



