from django import forms
from .models import JobPost
from tinymce.widgets import TinyMCE
from .choices import EMPLOYMENT_TYPE_CHOICES


# form for creatign a job post
class JobPostForm(forms.ModelForm):
	employment_type = forms.ChoiceField(choices=EMPLOYMENT_TYPE_CHOICES)
	description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))

	class Meta:
		model = JobPost
		exclude = ['user', 'company_account', 'last_updated', 'timestamp']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)	

		# adds the class form-control to every field in the form
		for field in self.fields:
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})








