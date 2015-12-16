# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.contrib.exporter import JsonItemExporter, JsonLinesItemExporter
import json
import csv



####################################################################
#class JsonWriterPipeline(object):
#
#
#    def process_item(self, item, spider):
#        self.file = open('%s_something.json' % spider.name, 'wb')
#        lines = json.dumps(dict(item)) + "\n"
#        self.file.write(lines)
#        return item
######################################################################


class JsonLinesExportPipeline(object):

    def __init__(self):
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        self.files = {}
        self.first_item = True

    def spider_opened(self, spider):
        file = open('%s_items.json' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = JsonLinesItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


#########################################################################
#class MyExporter(object):
#    def __init__(self):
#        self.myCSV = csv.writer(open('output-lipsum.csv', 'wb'))
#        self.myCSV.writerow(['title', 'paragraphs','headings'])
#
#    def process_item(self, item, spider):
#        self.myCSV.writerow([item['title'], item['paragraphs'], item['headings']])
#        return item
############################################################################