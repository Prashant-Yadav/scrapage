from django import forms
from fetch_data.models import ScrapWebpage

class URLForm(forms.ModelForm):
	class Meta:
		model = ScrapWebpage
		fields = ['page_url']
