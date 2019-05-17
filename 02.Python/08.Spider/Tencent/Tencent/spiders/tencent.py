# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    # 定义基准url，方便下面做url拼接
    url = 'https://careers.tencent.com/search.html?index='
    # offset = 1
    start_urls = ['https://careers.tencent.com/search.html?index=1']

    def parse(self, response):
        for i in range(2, 4):
            # print(self.url + str(i))
            yield scrapy.Request(self.url+str(i), callback=self.parse_page, dont_filter=True)

    def parse_page(self, response):
        # 每个职位节点对象列表
        base_list = response.xpath('//div[@class="search-content"]')
        for base in base_list:
            item = TencentItem()
            item['name'] = base.xpath('.//h4/text()').extract()[0]
            item['location'] = base.xpath('.//span[2]/text()').extract()[0]
            item['type'] = base.xpath('.//span[3]/text()').extract()[0]
            item['time'] = base.xpath('.//span[4]/text()').extract()[0]
            item['info'] = base.xpath('.//p[2]/text()').extract()[0]
            yield item




