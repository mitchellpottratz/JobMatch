from django.urls import path
from . import views

urlpatterns = [

	# where the candidate user completes their account information after registering	
	path('complete-info/', views.complete_info, name='complete_info')

]




