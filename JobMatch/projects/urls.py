from django.urls import path
from . import views

urlpatterns = [
	
	# where candidate users create a new project
	path('new/', views.new, name='new')
]