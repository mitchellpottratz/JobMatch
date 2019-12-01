from django.forms import ModelForm
from .models import Company


# this form is used to create a new company
class CompanyForm(ModelForm):

	class Meta:
		model = Company
		fields = ['name', 'image']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({
			'class': 'form-control'
		})
		# self.fields['image'].widget.attrs.update({
			
		# })




