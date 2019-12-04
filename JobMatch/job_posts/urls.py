from django.urls import path
from . import views

urlpatterns = [

	# where company users create job posts
	path('new/', views.new, name='new'),	

]


