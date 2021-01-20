from django.shortcuts import render

def index(request):
	"""Home page for Cypher."""
	return render(request, 'cypher_app/index.html')