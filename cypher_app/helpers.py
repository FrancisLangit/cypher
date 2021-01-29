"""Helpers module."""

import re

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
	"""Parses text from form object and returns a cipher or deciphered text.
	
	Args:
		cipher_choice (str): Choice of cipher. Based on CIPHER_DICT keys.
		form: Django form object that user fills up in page.
	Returns: 
		str: Output text. Either ciphered or deciphered dependent on user's ch
		oice of operation.
	"""
	# Detect if no key input from user in /app/caesar_cipher page.
	if cipher_choice == 'caesar_cipher' and not form.cleaned_data['key']:
		return (1, 'Error. No key input. Please indicate Caesar Cipher key.')

	# Create class object based on user's chosen cipher.
	cipher_object = _create_cipher_object(cipher_choice, form)

	# Return output text based on user's choice of operation.
	if form.cleaned_data['operation'] == 'cipher':
		return cipher_object.cipher()
	else:
		return cipher_object.decipher()


def _create_cipher_object(cipher_choice, form):
	"""Creates a cipher object from classes in CIPHER_DICT. Based on choice of
	cipher inputted by user in form. 
	
	Args:
		cipher_choice (str): Choice of cipher. Based on CIPHER_DICT keys.
		form: Django form object that user fills up in page.
	Returns: 
		class object: Cipher object from CIPHER_DICT based on choice of user.
	"""
	cipher_class = CIPHER_DICT[cipher_choice]
	if cipher_choice == 'caesar_cipher':
		return cipher_class(
			form.cleaned_data['text'], form.cleaned_data['key'])
	else:
		return cipher_class(form.cleaned_data['text'])


def mobile(request):
	"""Returns True if the request object comes from a mobile device.

	Adapted from bhaskarc's answer to StackOverflow post "Detect mobile device
	s with Django and Python 3" from https://stackoverflow.com/questions/42273
	319/detect-mobile-devices-with-django-and-python-3.

	Args:
		request: Request object from view.

	Returns:
		bool: True if request is from mobile device. False if otherwise.
	"""

	MOBILE_AGENT_RE = re.compile(
		r".*(iphone|mobile|androidtouch)", re.IGNORECASE)

	if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
	    return True
	else:
	    return False
