from django import forms
from tinymce.widgets import TinyMCE
from .models import Project


# form for creating a new project
class ProjectForm(forms.ModelForm):

	start_date = forms.DateTimeField(
		input_formats=['%d/%m/%Y'],
		widget=forms.DateTimeInput(attrs={
			'class': 'form-control datetimepicker-input',
			'data-target': '#datetimepicker1'
		})
	)
	end_date = forms.DateTimeField(
		input_formats=['%d/%m/%Y'],
		widget=forms.DateTimeInput(attrs={
			'class': 'form-control datetimepicker-input',
			'data-target': '#datetimepicker1'
		})
	)

	class Meta:
		model = Project
		exclude = ['user', 'last_updated', 'timestamp']


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# adds the class form-control to every field 
		for field in self.fields:
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

		self.fields['start_date'].widget.attrs.update({
			'type': 'date'
		})