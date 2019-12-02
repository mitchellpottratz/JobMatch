from django.forms import ModelForm
from .models import CandidateInfo


# form for the candidate users information
class CandidateInfoForm(ModelForm):

	class Meta:
		model = CandidateInfo
		exclude = ['user']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)	

		# adds the class form-control to every field in the form
		for field in self.fields:
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})




