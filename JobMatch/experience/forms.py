from django import forms
from .models import Experience
from tinymce.widgets import TinyMCE
from job_posts.choices import EMPLOYMENT_TYPE_CHOICES


# form for creating a new project
class ExperienceForm(forms.ModelForm):
	employment_type = forms.ChoiceField(choices=EMPLOYMENT_TYPE_CHOICES)
	description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))


	class Meta:
		model = Experience
		exclude = ['user', 'last_updated', 'timestamp']
		widgets = {
			'start_date': forms.DateInput(attrs={'type': 'date'}),
			'end_date': forms.DateInput(attrs={'type': 'date'}),
		}


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# adds the class form-control to every field 
		for field in self.fields:
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

		# add location-input id to the location field for google 
		# location autocomplete api
		self.fields['location'].widget.attrs.update({
			'id': 'location-input'
		})


