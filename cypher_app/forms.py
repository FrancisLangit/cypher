from django import forms

class InputTextForm(forms.Form):
	input_text = forms.CharField(label='Text', max_length=1000)
	