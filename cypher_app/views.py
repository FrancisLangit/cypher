from django.shortcuts import render 

from .forms import InputTextForm

def index(request):
	"""Home page for Cypher."""
	if request.method == 'POST':
		form = InputTextForm(request.POST)
		if form.is_valid():
			cipher = form.cleaned_data['input_text'] + 'yay'

			return render(
				request,
				'cypher_app/index.html',
				{
					'form': form,
					'cipher': cipher
				},
			)
	else:
		form = InputTextForm()

	return render(request, 'cypher_app/index.html', {'form': form})