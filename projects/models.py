from django.db import models
from django.utils import timezone
from django.conf import settings
from tinymce import models as tinymce_models 
from .managers import ProjectQuerySet


# represents a candidate users project
class Project(models.Model):
	 # user the project belongs to 
	 user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects')

	 # basic info about the project
	 title = models.CharField(max_length=150)
	 url = models.CharField(max_length=500, blank=True, null=True)
	 image = models.ImageField(upload_to='projects/')

	 # when the project started and ended
	 start_date = models.DateField()
	 end_date = models.DateField()

	 # who the project with with
	 associated_with = models.CharField(max_length=150)

	 # users description about the project
	 description = tinymce_models.HTMLField()

	 last_updated = models.DateTimeField(default=timezone.now()) 
	 timestamp = models.DateTimeField(default=timezone.now()) 

	 # query manager
	 objects = ProjectQuerySet.as_manager()

	 def __str__(self):
	 	return self.user.get_full_name() + ' - ' + self.title


