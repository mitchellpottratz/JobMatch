# django imports 
from django.shortcuts import render
from django.http import JsonResponse
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

	print('skill:', skill)

	return JsonResponse({'data': skill})









