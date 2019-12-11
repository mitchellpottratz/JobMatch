from django.db import models


# handles queries for Experience model
class ExperienceQuerySet(models.QuerySet):

	# returns all of a users experiences
	def get_users_experiences(self, user):
		return self.filter(user=user).order_by('-timestamp')







