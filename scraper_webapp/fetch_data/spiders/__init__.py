# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from twisted.internet import reactor
import scrapy
from scrapy.utils.project import get_project_settings
from fetch_data.items import WebpageScraperItem

#from models import ScrapWebpage

class MySpider(scrapy.Spider):
    # Your spider definition
    name="fetch_data"

    def __init__(self, *args, **kwargs):
    	super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('start_url')]

    def parse(self, response):
    	item = WebpageScraperItem()
    	item['title'] = response.xpath('//title/text()').extract()
    	item['paragraphs'] = response.xpath('//p/text()').extract()
    	item['headings'] = response.xpath('//h1/text()').extract()
    	return item