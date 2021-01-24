from django import forms

class CaesarCipherForm(forms.Form):
	text = forms.CharField(label='Text', max_length=1000)
	key = forms.IntegerField(min_value=0, max_value=26)