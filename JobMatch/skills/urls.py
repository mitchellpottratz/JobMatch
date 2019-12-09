from django.urls import path
from . import views

urlpatterns = [
	path('add/', views.add_candidate_skill, name='add_candidate_skill'),

	path('search/', views.search, name='search'),
]