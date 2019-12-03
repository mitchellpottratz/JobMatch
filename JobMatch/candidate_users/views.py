from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# model imports 
from .models import CandidateInfo

# form imports 
from .forms import CandidateInfoForm

# imports decorators that checks if the current user has their
# CandidateInfo model completed
from .decorators import no_candidate_info


# this is where the user fills out the rest of their information
# after they register
@login_required
@no_candidate_info
def complete_info(request):

	# if the form was submitted
	if request.method == 'POST':

		# passes the data into the form
		form = CandidateInfoForm(request.POST) 

		# if the form is valid
		if form.is_valid():
			# saves the form
			candidate_info = form.save(commit=False)
			candidate_info.user = request.user
			candidate_info.save()
			return redirect('/candidate/account/')

		# if the the form wasnt valid
		else:
			print('form is invalid')

	# if the form has not been submitted yet
	else:
		form = CandidateInfoForm()

	return render(request, 'candidate_info.html', {'form': form})







