# django imports 
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# model imports
from .models import Project
 
# form imports 
from .forms import ProjectForm

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


	
