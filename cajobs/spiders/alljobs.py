# -*- coding: utf-8 -*-
import scrapy


class AlljobsSpider(scrapy.Spider):
    name = "alljobs"
    allowed_domains = ["https://forms.spb.ca.gov/bulletins/showall.cfm"]
    start_urls = (
        'https://forms.spb.ca.gov/bulletins/showall.cfm/',
    )

    def parse(self, response):
        filename=response.url.split("/")[-2]
        #print filename
        #x=response.xpath("//table")[1].xpath("./tr")

        for sel in response.xpath("//table")[1].xpath("./tr"):
        	#print sel.xpath("./td/text()")
        	#job_title=sel.xpath("./td/text()")[0].extract()
        	#job_exams=sel.xpath("./td/text()")[1].extract()
        	#job_vacancies=sel.xpath("./td/text()")[2].extract()
        	
        	job_title=sel.xpath("./td/text()")[0].extract()
        	
        	try:
        		job_exams=sel.xpath("./td/a/text()")[0].extract()
        		job_vacancies=sel.xpath("./td/a/text()")[1].extract()

        		job_exams_link=sel.xpath("./td/a/@href")[0].extract() #relative path via cfm
        		jobs_vacancies_link=sel.xpath("./td/a/@href")[1].extract() #absolute path via 
        	except:
        		pass
        	#job_vacancies=sel.xpath("./td/text()")[2].extract()

        	#print job_title, job_exams
        	#print sel.xpath("./td/a/@href").extract() #this works!
        	#print type(sel.xpath("./td/a/text()").extract())
        	#print sel.xpath("./td/a/text()").extract()

        	try:
        		print job_exams,job_vacancies, job_exams_link, jobs_vacancies_link
        	except:
        		pass
        	#print type(sel.xpath("./td")[0]) #iam selector
        	#print job_exams
        	#print job_vacancies
