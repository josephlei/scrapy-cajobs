# -*- coding: utf-8 -*-
import scrapy


class AlljobsSpider(scrapy.Spider):
    name = "alljobs"
    allowed_domains = ["https://forms.spb.ca.gov/bulletins/showall.cfm"]
    start_urls = (
        'http://www.https://forms.spb.ca.gov/bulletins/showall.cfm/',
    )

    def parse(self, response):
        pass
