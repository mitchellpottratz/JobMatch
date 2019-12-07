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
		print('current skill being iterted over:', skill)

		# finds candidates with the matching skill
		candidates = CandidateInfo.objects.filter(skills__id=skill.id)
		print('candidates with matching skill: ', candidates)

		# add the candidates to the list
		[candidates_list.append(candidate) for candidate in candidates]
		

	print('candidates list:', candidates_list)

	return redirect('/company-account/')	





