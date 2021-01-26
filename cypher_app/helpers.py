"""Helpers module."""

# Import modules from local ciphers package.
from cypher_app.ciphers import (
	binary,
	caesar_cipher,
	morse_code,
	pig_latin,
)

# Dictionary pairing OtherCiphersForm cipher choices to their modules.
CIPHER_DICT = {
	"binary": binary.Binary,
	"caesar_cipher": caesar_cipher.CaesarCipher,
	"morse_code": morse_code.MorseCode,
	"pig_latin": pig_latin.PigLatin,
}


def parse_text(cipher_choice, form):
	"""Parses text from Django form object.
	
	Args:
		cipher_choice (str): Choice of cipher. Based on CIPHER_DICT keys.
		form: Django form object that user fills up in page.
	Returns: 
		str: Output text. Either ciphered or deciphered dependent on user's ch
		oice of operation.
	"""
	cipher_class = CIPHER_DICT[cipher_choice]
	if cipher_choice == 'caesar_cipher':
		cipher_object = cipher_class(
			form.cleaned_data['text'], form.cleaned_data['key'])
	else:
		cipher_object = cipher_class(form.cleaned_data['text'])

	if form.cleaned_data['operation'] == 'cipher':
		return cipher_object.cipher()
	else:
		return cipher_object.decipher()