from django.db import models


# query sets manager for the JobPost model
class JobPostQuerySet(models.QuerySet):
	
	# returns all of the job posts for a company
	def all_company_posts(self, company):
		return self.filter(company_account=company).order_by('timestamp')

