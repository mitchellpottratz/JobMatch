# django imports 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

# model imports
from .models import Project
 
# form imports 
from .forms import ProjectForm

# this view renders the ProjectForm and a candidate user can 
# create a new project
@login_required
def new(request):
	# if the form was submitted
	if request.method == 'POST':
		form = ProjectForm(request.POST, request.FILES)

		# if the form is valid 
		if form.is_valid():
			project = form.save(commit=False)
			project.user = request.user
			project.save()
			return redirect('/candidate-account/')

		# if the form is not valid
		else:
			print('form invalid')
			print(form.errors)

	# if the form hasnt been submitted
	else:
		form = ProjectForm()
	return render(request, 'projects/new.html', {'form': form})


# this view renders the ProjectForm and a canidate user can 
# edit one of their projects
def edit(request, id):
	user = request.user

	# get the user project by its id
	project = Project.objects.get(id=id)

	# if the user is not the owner of the project
	if project.user != user:
		raise PermissionDenied

	# if the form was submitted
	if request.method == 'POST':
		form = ProjectForm(request.POST, request.FILES, instance=project)

		# if the form is valid 
		if form.is_valid():
			form.save()
			return redirect('/candidate-account/')

		# if the form is not valid
		else:
			print('form invalid')
			print(form.errors)

	# if the form hasnt been submitted
	else:
		form = ProjectForm(instance=project)

	return render(request, 'projects/edit.html', {'form': form})



	
