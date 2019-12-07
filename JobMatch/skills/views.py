# django imports 
from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required

# model imports 
from .models import Skill
from candidate_users.models import CandidateInfo

# creates a new skill
@login_required
def add(request):

	# POST is the only method allowed for this view 
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

	return render(request, 'skills/new.html')


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











