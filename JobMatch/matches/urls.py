from django.urls import path 
from . import views

urlpatterns = [
	# here is where company users can see matches for one of their job posts
	path('<id>/', views.find_job_posts_matches, name='find_job_posts_matches'),
	
	# here matches are created for a job posts
	path('create/<id>/', views.create_matches, name='create_matches'),

	# here is where a company likes a candidate user
	path('like-candidate/<id>/', views.like_candidate, name='like_candidate'),

	# here is where a company dislikes a candidate user
	path('dislike-candidate/<id>/', views.dislike_candidate, name='dislike_candidate'),
]

