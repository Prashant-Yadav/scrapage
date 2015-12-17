# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#This model will be used to hold the data scraped from webpages
class WebpageScraperItem(scrapy.Item):
    title = scrapy.Field()
    #url = scrapy.Field()
    paragraphs = scrapy.Field()
    links = scrapy.Field()
    headings = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()