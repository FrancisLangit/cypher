from django import forms

class CaesarCipherForm(forms.Form):
	text = forms.CharField(label='Text', max_length=1000)
	key = forms.IntegerField(min_value=0, max_value=26)

class OtherCiphersForm(forms.Form):
	text = forms.CharField(label='Text', max_length=1000)
	cipher_choice = forms.ChoiceField(label='Choose Cipher', choices=(
		("binary", "Binary"),
		("morse_code", "Morse Code"),
		("pig_latin", "Pig Latin"),
	))