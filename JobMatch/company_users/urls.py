from django.urls import path
from . import views

urlpatterns = [
	
	# this is where company users can join a company with an invite code
	path('join/', views.join, name='join'),
]