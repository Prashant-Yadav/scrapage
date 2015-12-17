# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from twisted.internet import reactor

import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.linkextractors import LinkExtractor

from fetch_data.items import WebpageScraperItem


class MySpider(scrapy.Spider):
    # Your spider definition
    name="fetch_data"

    def __init__(self, *args, **kwargs):
    	super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('start_url')]
        self.link_extractor = LinkExtractor()

    def parse(self, response):
    	item = WebpageScraperItem()
    	item['title'] = response.xpath('//title/text()').extract()
    	item['paragraphs'] = response.xpath('//p/text()').extract()
    	item['headings'] = response.xpath('//h1/text()').extract()
        links = self.link_extractor.extract_links(response)
        item['links'] = [x.url for x in links]
        item['image_urls'] = response.xpath('//img/@src').extract()
    	return item