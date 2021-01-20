from django.shortcuts import render 

from .forms import InputTextForm

from cypher_app.ciphers.pig_latin import PigLatin

def index(request):
	"""Home page for Cypher."""
	if request.method == 'POST':
		form = InputTextForm(request.POST)
		if form.is_valid():
			input_text = form.cleaned_data['input_text']
			ciphered_text = PigLatin(input_text).cipher()
			return render(request, 'cypher_app/index.html', {
					'form': form,
					'ciphered_text': ciphered_text,
				},
			)
	else:
		form = InputTextForm()

	return render(request, 'cypher_app/index.html', {'form': form})