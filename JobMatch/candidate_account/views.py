# django imports 
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# model imports 
from projects.models import Project


@login_required
def index(request):
	# current user
	user = request.user

	# gets all of the users projects
	projects = Project.objects.get_users_projects(user)

	# dictionary passed into the template
	context = {
		'user': user,
		'projects': projects,
	}

	return render(request, 'candidate_account/index.html', context)
