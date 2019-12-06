from django.db import models


# handles querys for the Project model
class ProjectQuerySet(models.QuerySet):

	# returns all of a users projects
	def get_users_projects(self, user):
		return self.filter(user=user).order_by('-timestamp')







