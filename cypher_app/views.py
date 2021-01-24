from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CaesarCipherForm, OtherCiphersForm

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
	"morse_code": morse_code.MorseCode,
	"pig_latin": pig_latin.PigLatin,
}


def index(request):
	"""Index view of the website. 

	Defaults to redirecting the user to the app page of the website.
	"""
	return redirect('/app')


def app(request):
	"""App view of the website.

	Where the user can turn their text into a Caesar Cipher.
	"""
	if request.method == 'POST':
		form = CaesarCipherForm(request.POST)
		if form.is_valid():
			# Create CaesarCipher object with form data.
			ciphered_text = caesar_cipher.CaesarCipher(
				form.cleaned_data['text'], 
				form.cleaned_data['key'],
			).cipher()

			# Append ciphered text to messages.
			messages.add_message(request, messages.INFO, ciphered_text)
		return redirect('/app')
	else:
		form = CaesarCipherForm()
	return render(request, 'cypher_app/app.html', {'form': form})


def others(request):
	"""Others view of the website.

	User can access the other ciphering algorithms here.
	"""
	if request.method == 'POST':
		form = OtherCiphersForm(request.POST)
		if form.is_valid():
			cipher_class = CIPHER_DICT[form.cleaned_data['cipher_choice']]
			ciphered_text = cipher_class(form.cleaned_data['text']).cipher()
			messages.add_message(request, messages.INFO, ciphered_text)
		return redirect('app/others')
	else:
		form = OtherCiphersForm()
	return render(request, 'cypher_app/others.html', {'form': form})
