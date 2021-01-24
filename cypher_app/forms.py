from django import forms

class InputTextForm(forms.Form):
	text = forms.CharField(label='Text', max_length=1000)
	cipher = forms.ChoiceField(label='Cipher', choices=(
			("Binary", "Binary"),
			("Caesar Cipher", "Caesar Cipher"),
			("Morse Code", "Morse Code"),
			("Pig Latin", "Pig Latin"),
	))