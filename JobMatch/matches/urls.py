from django.urls import path 
from . import views

urlpatterns = [
	
	# here matches are created for a job posts
	path('create/<id>/', views.create_matches, name='create_matches'),


]

