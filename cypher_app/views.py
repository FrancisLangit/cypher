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
	return render(request, 'cypher_app/app_card_body_form.html', {
		'form': CipherTextForm(),
		'is_mobile': helpers.mobile(request),
	})


def app_output(request, form, cipher_choice):
	context = {
		'input_text': form.cleaned_data['text'],
		'key': form.cleaned_data['key'],
		'operation': form.cleaned_data['operation'],
		'output_text': helpers.parse_text(cipher_choice, form),
	}
	return render(request, 'cypher_app/app_card_body_output.html', context)


def about(request):
	"""About page.

	User can learn about the background of the project here.
	"""
	return render(request, 'cypher_app/about.html')