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
			output_text = helpers.parse_text(cipher_choice, form)
			messages.add_message(request, messages.INFO, output_text)
		return redirect('cypher_app:app', cipher_choice=cipher_choice)
	context = {
		'form': CipherTextForm(),
		'is_mobile': helpers.mobile(request),
	}
	return render(request, 'cypher_app/app.html', context)


def app_output(request, cipher_choice):
	return HttpResponse("Hello, world.")


def about(request):
	"""About page.

	User can learn about the background of the project here.
	"""
	return render(request, 'cypher_app/about.html')