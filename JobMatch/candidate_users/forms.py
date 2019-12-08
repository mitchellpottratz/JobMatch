from django.forms import ModelForm
from .models import CandidateInfo


# form for the candidate users information
class CandidateInfoForm(ModelForm):

	class Meta:
		model = CandidateInfo
		exclude = ['user', 'skills', 'last_updated', 'timestamp']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)	

		# adds the class form-control to every field in the form
		for field in self.fields:
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

		# add id to location field so it will use google location autocomplete
		self.fields['location'].widget.attrs.update({
			'id': 'location-input'
		})




