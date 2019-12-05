# django imports
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# import decorator that checks if current user is a company user
from company_account.decorators import company_account_required

# model imports 
from .models import JobPost

# form imports
from .forms import JobPostForm


@login_required
@company_account_required
def index(request):
	return render(request, 'job_posts/index.html')

# creates a job post
@login_required
@company_account_required
def new(request):

	# if the form was submitted
	if request.method == 'POST':

		form = JobPostForm(request.POST)
		print('job post form data:', request.POST)

		# if the form is valid
		if form.is_valid():
			job_post = form.save(commit=False)
			job_post.user = request.user
			job_post.company_account = request.user.company_account
			job_post.save()

		# if the form wasnt valid
		else:
			print('form validation error')

	# if the form wasnt submitted
	else:
		form = JobPostForm()

	return render(request, 'job_posts/new.html', {'form': form})











