# django imports 
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# model imports 
from projects.models import Project
from experience.models import Experience


@login_required
def index(request):
	# current user
	user = request.user

	# gets all of the users projects
	projects = Project.objects.get_users_projects(user)

	# gets all of the user experiences
	experiences = Experience.objects.get_users_experiences(user)

	# dictionary passed into the template
	context = {
		'user': user,
		'projects': projects,
		'experiences': experiences,
	}

	return render(request, 'candidate_account/index.html', context)
