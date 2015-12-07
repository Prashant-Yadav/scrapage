# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from webpage_scraper.items import WebpageScraperItem

class MySpider(scrapy.Spider):
    # Your spider definition
    name="webpage_scraper"
    start_urls = ['https://wikimediafoundation.org/wiki/Home']

    def parse(self, response):
    	item = WebpageScraperItem()
    	item['title'] = response.xpath('//title/text()').extract()
    	item['paragraphs'] = response.xpath('//p/text()').extract()
    	item['headings'] = response.xpath('//h1/text()').extract()
    	yield item

#configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
#runner = CrawlerRunner()

#d = runner.crawl(MySpider)
#d.addBoth(lambda _: reactor.stop())
#reactor.run() # the script will block here until the crawling is finished
