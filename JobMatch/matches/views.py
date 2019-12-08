# django imports
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

# import decorator that checks if current user is a company user
from company_account.decorators import company_account_required

# model imports 
from .models import Match
from job_posts.models import JobPost
from candidate_users.models import CandidateInfo
from company_users.models import Company


# this view is where company users are shown one candidate for a job post
# and they can either like or dislike that candidate
@login_required
@company_account_required
def show_candidate_match(request, id):
	# gets the job post
	job_post = get_object_or_404(JobPost, id=id)

	try:
		# gets a match for the job post
		match = Match.objects.get_job_post_match(job_post)

	# throws exception if there arent any matches left to view
	except Match.DoesNotExist:
		match = None

	# if there are still matches for the job post to view
	if match is not None:
		# gets the candidate user 
		candidate_user = match.candidate_user

		# gets the candidates user info 
		candidate_user_info = CandidateInfo.objects.get(user=candidate_user)

	# if there are not anymore matches to see for the job post
	else:
		candidate_user = None
		candidate_user_info = None

	# data being passed into the template
	context = {
		'job_post': job_post,
		'match': match,
		'candidate_user': candidate_user,
		'candidate_user_info': candidate_user_info
	}
	return render(request, 'matches/show_candidate_match.html', context)


# this view is where candidates are shown one job post and they either
# like or dislike the job post
@login_required
def show_job_post_match(request):
	user = request.user

	try:
		# gets a match for the candidate
		match = Match.objects.get_candidate_match(user)
		print('match:', match)

	# throws exception if there arent any matches left to view
	except Match.DoesNotExist:
		match = None

	# if the candidate user still has matches to view
	if match is not None:
		# gets the job post 
		job_post = match.job_post

		# gets the company the job belongs to 
		company = Company.objects.get(id=job_post.company_account.id)

	# if the candidate user does not have anymore job post matches to view
	else:
		job_post = None
		company = None

	# data being passed to the template
	context = {
		'match': match,
		'job_post': job_post,
		'company': company
	}
	return render(request, 'matches/show_job_post_match.html', context)


# this view is where matches are automatically generated right after a 
# job post is created
@login_required
@company_account_required
def create_matches(request, id):
	
	# gets the job posts 
	job_post = JobPost.objects.get(id=id)

	# gets all of the jobs posts skills
	job_post_skills = job_post.skills.all()

	# this list will store all of the canidates that match the skills 
	# on the job post
	candidates_list = []

	# iterate over all the skills in the job posting
	for skill in job_post_skills:

		# finds candidates with the matching location and skill
		candidates = CandidateInfo.objects.filter(location=job_post.location, skills__id=skill.id)

		# iterate through the matching candidates and add them to candidates_list
		# if they are not already in it
		for candidate in candidates:
			if candidate not in candidates_list:
				candidates_list.append(candidate)
		
	# iterate through the candidates and create a Match model for each candidate if the 
	# match doesnt already exist
	for candidate in candidates_list:
		if not Match.objects.does_match_exist(candidate.user, job_post):
			match = Match.objects.create(
				candidate_user=candidate.user,
				job_post=job_post
			)
			match.save()
		
	return redirect('/company-account/')	


# this view is where a candidate is liked by a company
@login_required
@company_account_required
def like_candidate(request, id):
	# gets the match
	match = get_object_or_404(Match, id=id)

	# change it so the company likes the candidate user and set
	# the value of the current company user
	match.company_liked	= True 
	match.company_user_liked = request.user
	match.save()

	# goes back to find matches page
	return redirect('/matches/' + str(match.job_post.id))


# this view is where a candidate is disliked by a company
@login_required
@company_account_required
def dislike_candidate(request, id):
	# gets the match
	match = get_object_or_404(Match, id=id)

	# change it so the company dislikes the candidate user and set
	# the value of the current company user
	match.company_liked	= False 
	match.company_user_liked = request.user
	match.save()

	# goes back to find matches page
	return redirect('/matches/')


# this view is where a job post is liked by a candidate
@login_required
def like_job(request, id):
	# gets the match
	match = get_object_or_404(Match, id=id)

	# change the value of the candidate like field to true to 
	# like the job
	match.candidate_liked = True 
	match.save()

	# goes back to find matches page
	return redirect('/matches/')


# this view is where a job post is liked by a candidate@login_required
@login_required
def dislike_job(request, id):
	# gets the match
	match = get_object_or_404(Match, id=id)

	# change the value of the candidate like field to false to 
	# dislike the job
	match.candidate_liked = False
	match.save()

	# goes back to find matches page
	return redirect('/matches/')
















