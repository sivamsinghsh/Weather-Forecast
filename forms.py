from django import forms

from .models import Individual


class IndivForm(forms.ModelForm):
	class Meta:
		 model = Individual
		 fields = [
		 	'First_name',
		 	'Last_name',
		 	'Email',
		 	'Phone',
		 	'gender',
		 	'address',	

		 ]