from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import InputTextForm

# Import cipher algorithms from ciphers package.
from cypher_app.ciphers.binary import Binary
from cypher_app.ciphers.caesar_cipher import CaesarCipher
from cypher_app.ciphers.morse_code import MorseCode
from cypher_app.ciphers.pig_latin import PigLatin

# def index(request):
# 	"""Home page for Cypher."""
# 	if request.method == 'POST':
# 		form = InputTextForm(request.POST)
# 		if form.is_valid():
# 			input_text = form.cleaned_data['input_text']
# 			ciphered_text = MorseCode(input_text).cipher()
# 			return render(request, 'cypher_app/index.html', {
# 					'form': form,
# 					'ciphered_text': ciphered_text,
# 				},
# 			)
# 	else:
# 		form = InputTextForm()

# 	return render(request, 'cypher_app/index.html', {'form': form})


def index(request):
	if request.method == 'POST':
		form = InputTextForm(request.POST)

		if form.is_valid():
			input_text = form.cleaned_data['input_text']
			ciphered_text = Binary(input_text).cipher()

			# return render(request, 'cypher_app/index.html', {
			# 		'form': form,
			# 		'ciphered_text': ciphered_text,
			# 	})
			messages.add_message(request, messages.INFO, ciphered_text)
			return redirect('/',)
	else:
		form = InputTextForm()
	return render(request, 'cypher_app/index.html', {'form': form})