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


def cipher_text(cipher_choice, form):
	"""Ciphers text from Django form object.
	
	Args:
		cipher_choice (str): Choice of cipher. Based on CIPHER_DICT keys.
		form: Django form object that user fills up in page.
	Returns: 
		str: Ciphered text.
	"""
	cipher_class = CIPHER_DICT[cipher_choice]
	if cipher_choice == 'caesar_cipher':
		return _text_to_caesar_cipher(cipher_class, form)
	else:
		return cipher_class(form.cleaned_data['text']).cipher()


def _text_to_caesar_cipher(cipher_class, form):
	"""Ciphers text from Django form object into a Caesar Cipher.

	Uses a try-except to catch TypeError exceptions resulting from there not b
	eing a "key" IntegerField input from user. 

	To be used within helpers.py module only.

	Args:
		form: Django form objects that user fills up in page.
	Returns:
		str: Ciphered text (or error if TypeError detected). 
	"""
	try:
		return cipher_class(
			form.cleaned_data['text'], 
			form.cleaned_data['key']).cipher()
	except TypeError:
		return 'No key input. Please indicate key.'

