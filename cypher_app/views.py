from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CaesarCipherForm, OtherCiphersForm

# Import CaesarCipher class from local ciphers package.
from cypher_app.ciphers import (
	binary,
	caesar_cipher,
	morse_code,
	pig_latin,
)

# Make dictionary pairing OtherCiphersForm cipher choices to their modules.
CIPHER_DICT = {
	"binary": binary.Binary,
	"morse_code": morse_code.MorseCode,
	"pig_latin": pig_latin.PigLatin,
}


def index(request):
	return redirect('/app')


def app(request):
	if request.method == 'POST':
		form = CaesarCipherForm(request.POST)
		if form.is_valid():
			ciphered_text = caesar_cipher.CaesarCipher(
				form.cleaned_data['text'], 
				form.cleaned_data['key'],).cipher()
			messages.add_message(request, messages.INFO, ciphered_text)
		return redirect('/app')
	else:
		form = CaesarCipherForm()
	return render(request, 'cypher_app/app.html', {'form': form})


def others(request):
	if request.method == 'POST':
		form = OtherCiphersForm(request.POST)
		if form.is_valid():
			cipher_choice = form.cleaned_data['cipher_choice']
			text = form.cleaned_data['text']

			cipher_module = CIPHER_DICT[cipher_choice]
			ciphered_text = cipher_module(text).cipher()
			
			messages.add_message(request, messages.INFO, ciphered_text)
		return redirect('/others')
	else:
		form = OtherCiphersForm()
	return render(request, 'cypher_app/others.html', {'form': form})
