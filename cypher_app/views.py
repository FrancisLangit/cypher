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
	context = {
		'form': CipherTextForm(),
		'current_cipher': helpers._get_cipher_name(cipher_choice),
		'is_mobile': helpers.mobile(request),
	}
	if request.method == 'POST':
		form = CipherTextForm(request.POST)
		if form.is_valid():		
			context['form'] = form
			context['output_text'] = helpers.parse_text(cipher_choice, form)
	return render(request, 'cypher_app/app.html', context)


def about(request):
	"""About page.

	User can learn about the background of the project here.
	"""
	return render(request, 'cypher_app/about.html')