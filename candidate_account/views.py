# django imports 
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# model imports 
from candidate_users.models import CandidateInfo
from projects.models import Project
from experience.models import Experience


@login_required
def index(request):
	# current user
	user = request.user

	# gets the users canidate info model instance
	user_info = CandidateInfo.objects.get(user=user)

	# gets all of the users projects
	projects = Project.objects.get_users_projects(user)

	# gets all of the users experiences
	experiences = Experience.objects.get_users_experiences(user)

	# gets all of the users skills
	skills = user_info.skills.all()

	# dictionary passed into the template
	context = {
		'user': user,
		'user_info': user_info,
		'projects': projects,
		'experiences': experiences,
		'skills': skills,
		'nav': 'account'
	}

	return render(request, 'candidate_account/index.html', context)
