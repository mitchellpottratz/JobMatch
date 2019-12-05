from django.urls import path
from . import views

urlpatterns = [

	# where company users can see all of their active
	# job posts
	path('', views.index, name='index'),

	# where company users create job posts
	path('new/', views.new, name='new'),	

]


