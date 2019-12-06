# django imports
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

# model imports 
from .models import Experience

# form imports 
from .forms import ExperienceForm

@login_required
def new(request):
	# if the form was submitted
	if request.method == 'POST':
		form = ExperienceForm(request.POST)

		# if the form is valid 
		if form.is_valid():
			experience = form.save(commit=False)
			experience.user = request.user
			experience.save()
			return redirect('/candidate-account/')

		# if the form is not valid
		else:
			print('form invalid')
			print(form.errors)

	# if the form hasnt been submitted
	else:
		form = ExperienceForm()
	return render(request, 'experience/new.html', {'form': form})






