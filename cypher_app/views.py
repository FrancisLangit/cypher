from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CipherTextForm

import cypher_app.helpers as helpers


def index(request):
	"""Index page. """
	ciphers = {
		'binary': 'Binary',
		'caesar_cipher': 'Caesar Cipher',
		'morse_code': 'Morse Code',
		'pig_latin': 'Pig Latin',
	}
	context = {'ciphers': ciphers}
	return render(request, 'cypher_app/index.html', context)


def app(request, cipher_choice):
	"""App page.

	Where the user can access app's ciphers.
	"""
	if request.method == 'POST':
		form = CipherTextForm(request.POST)
		if form.is_valid():
			output_text = helpers.parse_text(cipher_choice, form)
			messages.add_message(request, messages.INFO, output_text)
		return redirect('cypher_app:app', cipher_choice=cipher_choice)
	else:
		return render(request, 'cypher_app/app.html', {
			'form': CipherTextForm(), 'cipher_choice': cipher_choice,})


def about(request):
	"""About page.

	User can learn about the background of the project here.
	"""
	return render(request, 'cypher_app/about.html')