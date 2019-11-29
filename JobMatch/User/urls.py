from django.urls import path
from . import views

urlpatterns = [
	
	# path where users log into the app
	path('login/', views.login, name='login')	

]