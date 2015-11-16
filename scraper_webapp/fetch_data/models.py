from django.db import models

# Create your models here.

class Webpage(models.Model):
	#name = models.CharField(max_length=50)			
	title = models.CharField(max_length=70)			#stores title of webpage
	url = models.URLField()							#Stores the URL of the webpage
	paragraphs = models.TextField()					#Stores text content of the webpage
	links = models.URLField()						#Stores different links included on the webpage
	headings = models.CharField(max_length=200)		#Used to store different headings included on the webpage
	#images = models.ImageField()