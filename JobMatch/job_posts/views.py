# django imports
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# import decorator that checks if current user is a company user
from company_account.decorators import company_account_required

# model imports 
from .models import JobPost
from matches.models import Match 

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

			# redirects to url to create matches
			return redirect('/skills/create/job-post/' + str(job_post.id) + '/')

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
			# updated the job post
			job_post = form.save(commit=False)
			job_post.user = request.user
			job_post.last_updated = timezone.now()
			job_post.save()

			# redirects to url to create matches
			return redirect('/matches/create/' + str(job_post.id) + '/')

		# if the form wasnt valid
		else:
			print('form validation error')

	# if the form wasnt submitted
	else:
		form = JobPostForm(instance=job_post)

	return render(request, 'job_posts/edit.html', {'form': form})


# here is where companies can see all of the matches for a job post
# where they liked the candidate and the candidate like them
@login_required
@company_account_required
def show_matches(request, id):
	# gets the job post 
	job_post = get_object_or_404(JobPost, id=id)

	# gets all of the matches for the job post
	matches = Match.objects.get_job_post_matches(job_post)

	# data being passed to the template
	context = {
		'job_post': job_post,
		'matches': matches
	}
	return render(request, 'job_posts/show_matches.html', context)


# here is where companies can see one of there matches
@login_required
@company_account_required
def show_match(request, job_post_id, match_id):
	# gets the job post
	job_post = get_object_or_404(JobPost, id=job_post_id)

	# gets the match 
	match = get_object_or_404(Match, id=match_id)

	# gets the candidates info for the user the match is with
	candidate_info = match.candidate_user.candidate_info

	# gets the candidates skills
	skills = candidate_info.skills.all()

	# gets the candidate users experiences
	experiences = match.candidate_user.experiences.all()

	# gets the candidate users projects
	projects = match.candidate_user.projects.all()

	# data being passed to template
	context = {
		'job_post': job_post,
		'match': match,
		'candidate_info': candidate_info,
		'skills': skills,
		'experiences': experiences,
		'projects': projects
	}
	return render(request, 'job_posts/show_match.html', context)















