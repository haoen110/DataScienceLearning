# -*- coding: utf-8 -*-
import scrapy
from Daomu.items import DaomuItem

class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://www.daomubiji.com/dao-mu-bi-ji-1']

    def parse(self, response):
        # 创建item对象(items.py里的class)
        item = DaomuItem()
        # 匹配书名，单独匹配
        book = response.xpath('//h1[@class="focusbox-title"]/text()').extract()[0]
        # 匹配所有章节对象(基准xpath)
        articles = response.xpath('//article[@class="excerpt excerpt-c3"]')
        for article in articles:
            info = article.xpath('./a/text()').extract()[0].split(' ')
            # ['七星鲁王', '第一章', '血尸']
            item["book"] = book
            item["title"] = info[0]
            item["chapter"] = info[2]
            item["chapter_num"] = info[1]
            item["chapter_url"] = article.xpath('./a/@href').extract()[0]

            yield item
