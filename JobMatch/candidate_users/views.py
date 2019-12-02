from django.shortcuts import render
from django.http import HttpResponse

# model imports 
from .models import CandidateInfo

# form imports 
from .forms import CandidateInfoForm


# this is where the user fills out the rest of their information
# after they register
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







