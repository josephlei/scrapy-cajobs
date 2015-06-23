# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CajobsItem(scrapy.Item):
	job_title=scrapy.Field()
	job_exams=scrapy.Field()
	job_vacancies=scrapy.Field()
	job_exams_link=scrapy.Field()
	job_vacancies_link=scrapy.Field()
    # name = scrapy.Field()
    pass