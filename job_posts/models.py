from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models 
from django.conf import settings
from company_users.models import Company 
from skills.models import Skill 
from .managers import JobPostQuerySet


# this model represents a job post 
class JobPost(models.Model):

	# user that created the job post
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	# company the job post belongs to
	company_account = models.ForeignKey(Company, on_delete=models.CASCADE)

	# location of where the job is
	location = models.CharField(max_length=255, blank=True, null=True)

	# if the the job is remote, this will be true, and the city and state field
	# will be empty
	remote = models.BooleanField(default=False)

	# info about the job
	job_title = models.CharField(max_length=155)
	employment_type = models.CharField(max_length=75)
	description = tinymce_models.HTMLField() 
	industry = models.CharField(max_length=155)

	# skills needed for the job
	skills = models.ManyToManyField(Skill)

	# if the job has been posted yet
	active = models.BooleanField(default=True)

	# last time the job post was updated
	last_updated = models.DateTimeField(default=timezone.now())

	timestamp = models.DateTimeField(default=timezone.now())

	# query manager
	objects = JobPostQuerySet.as_manager()

	def __str__(self):
		return self.job_title
















