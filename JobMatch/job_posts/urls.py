from django.urls import path
from . import views

urlpatterns = [

	# where company users can see all their companies
	# job posts
	path('', views.all_job_posts, name='index'),

	# where company users create job posts
	path('new/', views.new_job_post, name='new'),	

	# where company users can edit a job post 
	path('edit/<id>/', views.update_job_post, name='update_job_post'),

	# where company users can see all of the matches for a job post
	path('<id>/matches/', views.show_matches, name='show_matches'),
]


