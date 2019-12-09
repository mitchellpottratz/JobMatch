# django imports 
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required

# model imports 
from .models import Skill
from candidate_users.models import CandidateInfo
from job_posts.models import JobPost


# creates a new skill for a candidate user
@login_required
def add_candidate_skill(request):
	# gets the current user
	user = request.user

	# gets all of the candidates skills
	users_skills = CandidateInfo.objects.get(user=user).skills.all()

	# if the form was submitted
	if request.method == 'POST':
		# gets the name of the skill
		name = request.POST.get('skill-name')

		# if the skills doesnt already exist
		if not Skill.objects.filter(name=name):
			# creates a new skill
			skill = Skill.objects.create(name=name)

		# if skill already exists
		else:
			# gets the skill by its naem
			skill = Skill.objects.get(name=name)

		# adds the skill to the candidate users skills field
		candidate_info = CandidateInfo.objects.get(user=request.user)
		candidate_info.skills.add(skill)
		candidate_info.save()

	# data being passed into the template
	context = {
		'user': user,
		'users_skills': users_skills
	}
	return render(request, 'skills/new.html', context)


# adds a skill to a job post
@login_required
def create_job_post_skill(request, id):
	# gets the current user
	user = request.user

	# gets the job post
	job_post = get_object_or_404(JobPost, id=id)

	# gets the job posts skills
	job_post_skills = job_post.skills.all()

	# if the form was submitted
	if request.method == 'POST':
		# gets the name of the skill
		name = request.POST.get('skill-name')

		# if the skills doesnt already exist
		if not Skill.objects.filter(name=name):
			# creates a new skill
			skill = Skill.objects.create(name=name)

		# if skill already exists
		else:
			# gets the skill by its naem
			skill = Skill.objects.get(name=name)

		# adds the skill to the job post
		job_post.skills.add(skill)
		job_post.save()

	# data being passed to template
	context = {
		'user': user,
		'job_post': job_post,
		'job_post_skills': job_post_skills,
	}
	return render(request, 'skills/new_job_post_skill.html', context)



# searches through the skills
@login_required
def search(request):

	# get the search string from the ajax call
	skill = request.GET.get('skill_string')

	# searches for skills based on the string
	results = Skill.objects.filter(name__icontains=skill)

	# converts the results to a list of skill names
	results_list = [model_to_dict(result)['name'] for result in results]

	return JsonResponse({'results': results_list})


@login_required
def delete_skill(request, name):
	# gets the current user
	user = request.user

	data = {}

	# if the method is post
	if request.method == 'POST':

		# if it is a candidate user deleting the skill
		if user.candidate_user:
			# deletes the skill from the candidate users candidate info
			candidate_skill = CandidateInfo.objects.get(user=user).skills.remove(
				Skill.objects.get(name=name)
			)
			data = {
				'message': 'Skill successfully deleted'
			}

		# if it is a company user deleting a skill from a job post
		else:
			print('company user deleting skill')

			# removes the skill from the job post
			job_post_skill = JobPost.objects.get(id=request.POST.get('data_id')).skills.remove(
				Skill.objects.get(name=name)
			)
			data = {
				'message': 'Skill successfully deleted from job post'
			}

	# if the method is not post
	else:
		data = {
			'message': 'Method not allowed'
		}

	return JsonResponse(data)












