from django.db import models


class MatchQuerySet(models.QuerySet):

	# checks if a match already exists for a candidate user and a job post
	def does_match_exist(self, candidate, job_post)
		return self.filter(candidate=candidate, job_post=job_post)



