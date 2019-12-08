from django.urls import path 
from . import views

urlpatterns = [
	# here is where company users can see matches for one of their job posts
	path('<id>/', views.show_candidate_match, name='show_candidate_match'),

	# here is where candidate users can see job post matches
	path('', views.show_job_post_match, name='show_job_post_match'),
	
	# here matches are created for a job posts
	path('create/<id>/', views.create_matches, name='create_matches'),

	# here is where a company likes a candidate user
	path('like-candidate/<id>/', views.like_candidate, name='like_candidate'),

	# here is where a company dislikes a candidate user
	path('dislike-candidate/<id>/', views.dislike_candidate, name='dislike_candidate'),

	# here is where a candidate user likes a job post
	path('like-job/<id>/', views.like_job, name='like_job'),

	# here is where a candidate user dislikes a job post
	path('dislike-job/<id>/', views.dislike_job, name='dislike_job'),

	# here is where companies are notified when they get a match
	path('company/match/<id>/', views.company_match, name='company_match'),

	# here is where candidates are notified when they get a match
	path('candidate/match/<id>/', views.candidate_match, name='candidate_match')
]

