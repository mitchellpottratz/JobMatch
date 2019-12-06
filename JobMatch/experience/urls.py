from django.urls import path
from . import views

urlpatterns = [
	
	# where candidate users create a new experience
	path('/new', views.new, name='new')

]




