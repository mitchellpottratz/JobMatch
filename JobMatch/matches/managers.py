from django.db import models


class MatchQuerySet(models.QuerySet):

	# checks if a match already exists for a candidate user and a job post
	def does_match_exist(self, candidate_user, job_post):
		return self.filter(candidate_user=candidate_user, job_post__id=job_post.id)

	# gets all of the matches for a job post
	def get_job_post_matches(self, job_post):
		return self.filter(job_post=job_post)



