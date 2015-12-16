from django.shortcuts import render
from django.http import HttpResponse
import os
import json

from .forms import URLForm
from spiders import MySpider
#from spiders import runCrawler

def index(request):	
	return  render(request, 'fetch_data/index.html', { 'form': URLForm(), })


def get_url(request):
	if request.method == 'POST' :
		form = URLForm(request.POST)
		if form.is_valid():
			form.save()
			url = form.cleaned_data['page_url']
			os.system("scrapy crawl fetch_data -a start_url="+url)
			data = json.loads(open('fetch_data_something.json').read())
			title = data['title']
			headings = data['headings']
			links = data['links']
			paragraphs = data['paragraphs']
			return render(request, 'fetch_data/get_url.html', { 'title':title, 'headings':headings, 'links':links, 'paragraphs':paragraphs, })

	return  HttpResponse("Form submission failed.")
	#else:
	#	form = URLForm()
	
def thank(request):
	return HttpResponse("Form submission successfull.")
