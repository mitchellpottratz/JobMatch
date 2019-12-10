from django.db import models
from django.contrib.auth.models import AbstractUser
from company_users.models import Company
from django.utils import timezone


# User model
# costumizes django's default User model
class User(AbstractUser):
	username = models.CharField(max_length=155, unique=True, blank=True)

	# profile picture
	image = models.ImageField(upload_to='users/', default='users/default_profile_picure.png')

	# if the user is apart of a company, a user that creates 
	# job postings for a company
	company_user = models.BooleanField(default=False)

	# if the use is just a candidate user, a user that is just
	# looking for job.
	candidate_user = models.BooleanField(default=False)

	# the company the user is apart of, this field is only used if the user is a company_user
	company_account = models.ForeignKey(
		Company,
		related_name='users',
		blank=True,
		null=True, 
		on_delete=models.CASCADE)

	# makes the email field all required
	email = models.EmailField(unique=True)

	# if the user has confirmed their email address
	email_confirmed = models.BooleanField(default=False)

	# returns users first and last name
	def get_full_name(self):
		return self.first_name + ' ' + self.last_name

	# returns the users username with @ prepended
	def format_username(self):
		return '@' + self.username







