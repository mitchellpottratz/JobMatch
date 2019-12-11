from django.urls import path
from . import views

urlpatterns = [
	
	# this is where company users can join a company with an invite code
	path('join/', views.join, name='join'),

	# this is where company users can create a new company
	path('new/', views.create_company, name='create_company'),

	path('/company', views.new_company, name='new_company')

]