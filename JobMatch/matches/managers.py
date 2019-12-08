from django.db import models


class MatchQuerySet(models.QuerySet):

	# checks if a match already exists for a candidate user and a job post
	def does_match_exist(self, candidate_user, job_post):
		return self.filter(candidate_user=candidate_user, job_post=job_post)

	# returns a candidate for a job post the company has seen yet
	def get_job_post_match(self, job_post):
		return self.filter(
			job_post=job_post, 
			company_liked=None, 
		).first()



