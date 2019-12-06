from django.urls import path
from . import views

urlpatterns = [
	
	# where candidate users create a new experience
	path('new/', views.new, name='new'),

	# where candidate users can edit an experience
	path('edit/<id>/', views.edit, name='edit')

]




