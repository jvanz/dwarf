# -*- coding: utf-8 -*-

import scrapy
from scrapy.linkextractors import LinkExtractor

class LinkSpider(scrapy.Spider):
    name = "link-spider"
    link_extractor = LinkExtractor()
    start_urls = [ "http://google.com" ]

    def parse(self, response):
        for link in self.link_extractor.extract_links(response):
            yield {
                    'source': response.request.url,
                    'destination': link.url
                    }
