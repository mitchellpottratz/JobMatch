# django imports
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict

# import decorator that checks if current user is a company user
from company_account.decorators import company_account_required

# model imports 
from .models import Match
from job_posts.models import JobPost
from candidate_users.models import CandidateInfo


# this view is where company users can look through candidates
# for a job post
@login_required
@company_account_required
def find_job_posts_matches(request, id):
	# gets the job post
	job_post = get_object_or_404(JobPost, id=id)

	# gets all matches for the job post
	match = Match.objects.get_job_post_match(job_post)
	print(match)

	# gets the candidate user 
	candidate_user = match.candidate_user
	print(candidate_user.username)

	# gets the candidates user info 
	candidate_user_info = CandidateInfo.objects.get(user=candidate_user)

	# data being passed into the template
	context = {
		'job_post': job_post,
		'match': match,
		'candidate_user': candidate_user,
		'candidate_user_info': candidate_user_info
	}
	return render(request, 'matches/find_job_posts_matches.html', context)


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



@login_required
@company_account_required
def dislike_candidate(request, id):
	pass





