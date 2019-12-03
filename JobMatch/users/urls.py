from django.urls import path
from . import views

urlpatterns = [

	# user registration
	path('register/', views.register, name='register'),

	# user login
	path('login/', views.login, name='login')

]


