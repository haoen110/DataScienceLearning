# -*- coding: utf-8 -*-
import scrapy
# from 包名.模块名 import 类
from csdn.items import CsdnItem

class CsdnSpider(scrapy.Spider):
    # 爬虫名，运行爬虫时使用
    name = 'CSDN'
    allowed_domains = ['blog.csdn.net']
    # 起始url，可以修改
    start_urls = ['https://blog.csdn.net/qq_42231391/article/details/83506181']

    def parse(self, response):
        item = CsdnItem()
        # 不加/text()出现的是选择器对象且包含节点所有内容[<selector .., data ='<h1>...</h1>']
        # 若加/text()也是得到选择器对象（节点文本）[selector ..., data='文本']
        # extract将选择器对象中文本取出来['文本内容']
        item["name"] = response.xpath('//h1[@class="title-article"]/text()').extract()[0]  # 把匹配出的对象转为字符串
        item["time"] = response.xpath('//span[@class="time"]/text()').extract()[0]
        item["count"] = response.xpath('//span[@class="read-count"]/text()').extract()[0]

        yield item
