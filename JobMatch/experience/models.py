from django.db import models
from django.utils import timezone
from django.conf import settings
from tinymce import models as tinymce_models 


# represents a candidate users experience
class Experience(models.Model):
	# user the experience belongs to 
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	# info about the experience
	title = models.CharField(max_length=150)
	company = models.CharField(max_length=150)
	employment_type = models.CharField(max_length=150)
	location = models.CharField(max_length=150)
	description = tinymce_models.HTMLField()

	# when the experience started and ended
	start_date = models.DateField()
	end_date = models.DateField()

	last_updated = models.DateTimeField(default=timezone.now()) 
	timestamp = models.DateTimeField(default=timezone.now()) 

	def __str__(self):
		return self.user.get_full_name + ' - ' + self.title




