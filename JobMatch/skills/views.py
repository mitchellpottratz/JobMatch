# django imports 
from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required

# model imports 
from .models import Skill

# creates a new skill
def create(request):

	# POST is the only method allowed for this view 
	if request.method == 'POST':

		# gets the name of the skill
		name = request.POST.get('name')

		# if the skills doesnt already exist
		if not Skill.objects.filter(name__iexact=name):

			# creates a new skill
			skill = Skill.objects.create(name=name)

			return JsonResponse(
				{'message': 'Skill added'}
			)

		else:
			return JsonResponse(
				{'message': 'That skill already exists'}
			)


# searches through the skills
def search(request):

	# get the search string from the ajax call
	skill = request.GET.get('skill_string')

	# searches for skills based on the string
	results = Skill.objects.filter(name__icontains=skill)

	# converts the results to a list of skill names
	results_list = [model_to_dict(result)['name'] for result in results]

	return JsonResponse({'results': results_list})









