from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CaesarCipherForm

# Import CaesarCipher class from local ciphers package.
from cypher_app.ciphers.caesar_cipher import CaesarCipher


def index(request):
	return redirect('/caesar_cipher')


def caesar_cipher(request):
	if request.method == 'POST':
		form = CaesarCipherForm(request.POST)
		if form.is_valid():
			ciphered_text = CaesarCipher(
				form.cleaned_data['text'], 
				form.cleaned_data['key'],).cipher()
			messages.add_message(request, messages.INFO, ciphered_text)
		return redirect('/caesar_cipher')
	else:
		form = CaesarCipherForm(request.POST)
	return render(request, 'cypher_app/caesar_cipher.html', {'form': form})