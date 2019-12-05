# django imports
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# import decorator that checks if current user is a company user
from company_account.decorators import company_account_required

# model imports 
from .models import JobPost

# form imports
from .forms import JobPostForm


# this view renders the page where company users can view
# all of the job post for their company
@login_required
@company_account_required
def all_job_posts(request):

	# gets all of the job posts
	job_posts = JobPost.objects.all_company_posts(request.user.company_account)

	return render(request, 'job_posts/index.html', {'job_posts': job_posts})


# this view renders a page where company users can create 
# a new job post
@login_required
@company_account_required
def new_job_post(request):

	# if the form was submitted
	if request.method == 'POST':
		form = JobPostForm(request.POST)

		# if the form is valid
		if form.is_valid():
			job_post = form.save(commit=False)
			job_post.user = request.user
			job_post.company_account = request.user.company_account
			job_post.save()
			return redirect('/job-posts/')

		# if the form wasnt valid
		else:
			print('form validation error')

	# if the form has not been submitted
	else:
		form = JobPostForm()

	return render(request, 'job_posts/new.html', {'form': form})


# this view renders a page where company users can edit a job post
@login_required
@company_account_required
def update_job_post(request, id):

	# gets the job post
	job_post = JobPost.objects.get(id=id)
	
	# if the form was submitted
	if request.method == 'POST':
		form = JobPostForm(request.POST, instance=job_post)

		# if the form is valid
		if form.is_valid():
			form.save()
			return redirect('/job-posts/')

		# if the form wasnt valid
		else:
			print('form validation error')

	# if the form wasnt submitted
	else:
		form = JobPostForm(instance=job_post)

	return render(request, 'job_posts/edit.html', {'form': form})

















