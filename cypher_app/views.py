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


def index(request):
	if request.method == 'POST':
		form = InputTextForm(request.POST)

		if form.is_valid():
			# Cipher text from user.
			input_text = form.cleaned_data['input_text']
			ciphered_text = morse_code.MorseCode(input_text).cipher()

			# Redirect user to page with ciphered text.
			messages.add_message(request, messages.INFO, ciphered_text)
			return redirect('/',)
	else:
		form = InputTextForm()
	return render(request, 'cypher_app/index.html', {'form': form})