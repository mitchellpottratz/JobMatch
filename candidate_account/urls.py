from django.urls import path
from .import views 

urlpatterns = [

	# candidate users account info page
	path('', views.index, name='index')

]

