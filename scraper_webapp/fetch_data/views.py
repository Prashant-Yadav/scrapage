from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return render(request, 'fetch_data/index.html')
