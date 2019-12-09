from django.urls import path
from . import views

urlpatterns = [
	
	# here is where a candidate can add skills
	path('add/', views.add_candidate_skill, name='add_candidate_skill'),

	# this is where skills are searched for
	path('search/', views.search, name='search'),

	# this is where skills can be deleted from either a candidate user
	# or a job post
	path('delete/<id>/', views.delete_skill, name='delete_skill')
]