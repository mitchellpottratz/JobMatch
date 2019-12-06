# django imports 
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
	user = request.user

	return render(request, 'candidate_account/index.html', {'user': user})
