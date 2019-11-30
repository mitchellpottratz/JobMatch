from django.urls import path
from . import views

urlpatterns = [

	# users register here
	path('register/', views.register, name='register'),

]


