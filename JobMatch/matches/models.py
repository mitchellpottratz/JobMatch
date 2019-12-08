from django.db import models
from django.utils import timezone
from django.conf import settings
from job_posts.models import JobPost
from .managers import MatchQuerySet


class Match(models.Model):
	# candidate user that is a potential match for the job
	candidate_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='matches')

	# the job post the match is associated with
	job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, null=True, blank=True, unique=False)

	# if the company liked the candidate
	company_liked = models.BooleanField(blank=True, null=True)

	# the company user that liked the candidate, is blank if the company didnt/hasnt liked the candidate
	company_user_like = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		blank=True,
		null=True,
		related_name='liked_matches'
	)

	# if the candidate liked the job post
	candidate_liked = models.BooleanField(blank=True, null=True)

	# the time the company liked the candidate
	company_liked_timestamp = models.DateTimeField(blank=True, null=True)

	# the time the candidate liked the job post
	candidate_liked_timestamp = models.DateTimeField(blank=True, null=True)

	timestamp = models.DateTimeField(default=timezone.now())

	# query set manager
	objects = MatchQuerySet.as_manager()

	def __str__(self):
		return self.candidate_user.get_full_name()



