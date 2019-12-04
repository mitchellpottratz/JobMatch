from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# this view is where a company user can view all
# of their information
@login_required
def index(request):
	return render(request, 'index.html')


