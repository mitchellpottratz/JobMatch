from django import forms
from .models import Project
from tinymce.widgets import TinyMCE


# form for creating a new project
class ProjectForm(forms.ModelForm):
	description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))

	class Meta:
		model = Project
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

		# add boostrap image style to file input
		self.fields['image'].widget.attrs.update({
			'class': 'custom-file-input'
		})