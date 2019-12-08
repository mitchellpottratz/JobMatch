from django.urls import path 
from . import views

urlpatterns = [
	# here is where company users can see matches for one of their job posts
	path('<id>/', views.find_job_posts_matches, name='find_job_posts_matches'),
	
	# here matches are created for a job posts
	path('create/<id>/', views.create_matches, name='create_matches'),
]

