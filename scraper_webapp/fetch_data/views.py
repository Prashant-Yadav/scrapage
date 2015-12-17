from django.shortcuts import render
from django.http import HttpResponse
import os
import json
import tempfile
import zipfile
from django.views import generic
from django.core.servers.basehttp import FileWrapper


from .forms import URLForm
from spiders import MySpider
from .models import Webpage


def index(request):	
	return  render(request, 'fetch_data/index.html', { 'form': URLForm(), })


def get_url(request):
	if request.method == 'POST' :
		form = URLForm(request.POST)
		if form.is_valid():
			form.save()
			url = form.cleaned_data['page_url']
			os.system("scrapy crawl fetch_data -a start_url="+url)
			data = json.loads(open('fetch_data_items.json').read())
			title = data['title']
			headings = data['headings']
			links = data['links']
			paragraphs = data['paragraphs']
			return render(request, 'fetch_data/get_url.html', { 'title':title, 'headings':headings, 'links':links, 'paragraphs':paragraphs, })

	return  HttpResponse("Form submission failed.")

	
class DownloadsView(generic.TemplateView):
	template_name = 'fetch_data/downloads.html'

def generate_text_files(request):
	data = json.loads(open('fetch_data_items.json').read())
	title = data['title']
	headings = data['headings']
	links = data['links']
	paragraphs = data['paragraphs']

	with open('content.txt', 'w') as f:
		f.write("Page title: \n")
		for t in title:
			f.write(t+"\n")
		
		f.write("\nPage headings: \n")
		for heading in headings:
			f.write(heading+"\n")
		
		f.write("\nParagraphs: \n")
		for para in paragraphs:
			f.write(para+"\n")
		
		i = 0
		f.write("\nLinks: \n")
		for l in links:
			i+=1
			f.write(str(i)+". "+l+"\n")

	filename = 'content.txt' # Select your file here.                                
	wrapper = FileWrapper(file(filename))
	response = HttpResponse(wrapper, content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename=content.txt'
	response['Content-Length'] = os.path.getsize(filename)
	return response

def dowload_images(request):
	