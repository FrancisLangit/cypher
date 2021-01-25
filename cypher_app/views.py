from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CipherTextForm

import cypher_app.helpers

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
			ciphered_text = cypher_app.helpers.cipher_text(
				cipher_choice, form)
			messages.add_message(request, messages.INFO, ciphered_text)
		return redirect('cypher_app:app', cipher_choice=cipher_choice)
	else:
		context = {
			'form': CipherTextForm(),
			'cipher_choice': cipher_choice,
		}
	return render(request, 'cypher_app/app.html', context)