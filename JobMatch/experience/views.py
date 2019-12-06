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
	return render(request, 'experience/new.html')
