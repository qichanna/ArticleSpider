# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.http import Request
from urllib import parse


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/110287/']

    def parse(self, response):
        re_selector = response.xpath('//*[@id="post-114405"]/div[1]/h1/text()')
        print(re_selector.extract())
