from django.db import models


# model class to store link of the page to be scraped, it should be filled through user 
# submission at fetch_data app....
class ScrapWebpage(models.Model):
	name = models.CharField(max_length=70)		#stores name of the webpage, which is usually the title
	page_url = models.URLField()				#stores url of webpage to be scraped

# model to store data which are scraped from the specified webapage
class Webpage(models.Model):
	#name = models.CharField(max_length=50)			
	title = models.CharField(max_length=70)			#stores title of webpage
	url = models.URLField()							#Stores the URL of the webpage
	paragraphs = models.TextField()					#Stores text content of the webpage
	links = models.URLField()						#Stores different links included on the webpage
	headings = models.CharField(max_length=200)		#Used to store different headings included on the webpage
	#images = models.ImageField()