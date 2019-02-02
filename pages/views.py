from django.shortcuts import render

# Create your views here.

def index(request): # home

	context = {
		'title' : '',
		'username' : 'Wolf',
	}

	return render(request, 'index.html', context)