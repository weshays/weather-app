from django import forms
from .models import ModelF

class FormF(forms.ModelForm):
	class Meta:
		model = ModelF
		fields = [
			"title",
			"description",
		]
