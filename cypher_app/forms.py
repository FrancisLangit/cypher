from django import forms


class CipherTextForm(forms.Form):
	text = forms.CharField(label='Text', max_length=1000)
	key = forms.IntegerField(
		label='Key', min_value=0, max_value=26, required=False)
	operation = forms.ChoiceField(
		label='Cipher or Decipher',
		choices=(
			('cipher', "Cipher"),
			('decipher', "Decipher"),
		))

