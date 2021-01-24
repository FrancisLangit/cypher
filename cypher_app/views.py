from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import InputTextForm

# Import cipher algorithms from local ciphers package.
from cypher_app.ciphers import (
	binary, 
	caesar_cipher, 
	morse_code, 
	pig_latin,
)

# Cipher choices presented to user and their actual modules. 
CIPHERS = {
	"Binary": binary.Binary,
	"Caesar Cipher": caesar_cipher.CaesarCipher,
	"Morse Code": morse_code.MorseCode,
	"Pig Latin": pig_latin.PigLatin,
}


def index(request):
	return redirect('/app')


def app(request):
	if request.method == 'POST':
		form = InputTextForm(request.POST)
		if form.is_valid():
			# Cipher user's text based on choice of cipher.
			cipher = CIPHERS[form.cleaned_data['cipher']]
			ciphered_text = cipher(form.cleaned_data['text']).cipher()

			# Redirect user to app page with ciphered text.
			messages.add_message(request, messages.INFO, ciphered_text)
			return redirect('/app')
	else:
		form = InputTextForm()
	return render(request, 'cypher_app/app.html', {'form': form})
