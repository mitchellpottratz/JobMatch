# django imports
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# import decorator that checks if current user is a company user
from company_account.decorators import company_account_required

# model imports 

# form imports
from .forms import JobPostForm

# creates a job post
@login_required
@company_account_required
def new(request):

	# if the form was submitted
	if request.method == 'POST':

		form = JobPostForm(request.POST)

		# if the form is valid
		if form.is_valid():
			pass

		# if the form wasnt valid
		else:
			pass

	# if the form wasnt submitted
	else:
		form = JobPostForm()

	return render(request, 'job_posts/new.html', {'form': form})