from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from subprocess import call
import os

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
			#spider = MySpider(url)
			#spider.runCrawler()
			#call(["scrapy", "crawl", "spider", "-o", "output.json"])
			os.system("scrapy crawl fetch_data -a start_url="+url+" -o output-lorel.json")
			return render(request, 'fetch_data/get_url.html')

	return  HttpResponse("Form submission failed.")
	#else:
	#	form = URLForm()
	
def thank(request):
	return HttpResponse("Form submission successfull.")
