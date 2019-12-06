from django import forms
from tinymce.widgets import TinyMCE
from .models import Experience


# form for creating a new project
class ExperienceForm(forms.ModelForm):
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


