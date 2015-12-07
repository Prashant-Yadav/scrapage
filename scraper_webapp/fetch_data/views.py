from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import URLForm


def index(request):	
	return  render(request, 'fetch_data/index.html', { 'form': URLForm(), })


def get_url(request):
	if request.method == 'POST' :
		form = URLForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('fetch_data:thank'))

	return  HttpResponse("Form submission failed.")
	#else:
	#	form = URLForm()
	
def thank(request):
	return HttpResponse("Form submission successfull.")
