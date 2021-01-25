from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CipherTextForm

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


def index(request):
	"""Index view of the website. 

	Defaults to redirecting the user to the app page of the website.
	"""
	return render(request, 'cypher_app/base.html')


def app(request, cipher_choice):
	"""App view of the website.

	Where the user can access app's ciphers.
	"""
	if request.method == 'POST':
		form = CipherTextForm(request.POST)
		if form.is_valid():
			ciphered_text = cipher_text(cipher_choice, form)
			messages.add_message(request, messages.INFO, ciphered_text)
		return redirect('cypher_app:app', cipher_choice=cipher_choice)
	else:
		context = {
			'form': CipherTextForm(),
			'cipher_choice': cipher_choice,
		}
	return render(request, 'cypher_app/app.html', context)


def cipher_text(cipher_choice, form):
	cipher_class = CIPHER_DICT[cipher_choice]
	if cipher_choice == 'caesar_cipher':
		return cipher_class(
			form.cleaned_data['text'], 
			form.cleaned_data['key']).cipher()
	else:
		return cipher_class(form.cleaned_data['text']).cipher()