from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CipherTextForm

import cypher_app.helpers as helpers


def index(request):
	"""Index.

	URL with no path after domain name redirects to /app/binary/ by default.
	"""
	return redirect('/app/binary/')


def app(request, cipher_choice):
	"""App page.

	Where the user can access app's ciphers.
	"""
	if request.method == 'POST':
		form = CipherTextForm(request.POST)
		if form.is_valid():		
			return app_output(request, form, cipher_choice)
	context = {
		'form': CipherTextForm(),
		'current_cipher': helpers._get_cipher_name(cipher_choice),
		'is_mobile': helpers.mobile(request),
	}
	return render(request, 'cypher_app/app.html', context)


def app_output(request, form, cipher_choice):
	"""App output view. 

	Updates app page when user submits form.
	"""
	context = {
		'form': CipherTextForm(request.POST),
		'current_cipher': helpers._get_cipher_name(cipher_choice),
		'output_text': helpers.parse_text(cipher_choice, form),
		'is_mobile': helpers.mobile(request),
	}
	return render(request, 'cypher_app/app.html', context)


def about(request):
	"""About page.

	User can learn about the background of the project here.
	"""
	return render(request, 'cypher_app/about.html')