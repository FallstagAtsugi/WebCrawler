# -*- coding: utf-8 -*-
import scrapy


class SamuraiSpider(scrapy.Spider):
    name = 'samurai'
    allowed_domains = ['www.sejuku.net']
    start_urls = [
        'https://www.sejuku.net/blog/',
        'https://www.sejuku.net/blog/recommends',
    ]

    def parse(self, response):
        print('#'*50)
        print(response.url)
        print(response.text)
