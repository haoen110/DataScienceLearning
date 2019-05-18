# -*- coding: utf-8 -*-
import scrapy


class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['cnblogs.com']
    # start_urls = ['http://cnblogs.com/']
    def start_requests(self):
        url = "https://www.cnblogs.com/"
        yield scrapy.FormRequest(url=url, formdata={"account": "haoen110", "password": "Howie1996925!"}, callback=self.parse_page)

    def parse_page(self, response):
        with open("test.html", "w") as f:
            f.write(response.text)
