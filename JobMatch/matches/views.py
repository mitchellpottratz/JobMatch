# django imports
from django.shortcuts import render, redirect
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
	return render(request, 'find_job_posts_matches.html')


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
		
	print('candidates list:', candidates_list)
	print('job post:', job_post)
	# iterate through the candidates and create a Match model for each candidate
	for candidate in candidates_list:

		# if not Match.objects.filter()
		match = Match.objects.create(
			candidate_user=candidate.user,
		)
		match.job_post = job_post
		match.save()
		print('match created:', match)

	return redirect('/company-account/')	





