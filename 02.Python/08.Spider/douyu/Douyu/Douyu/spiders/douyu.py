# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['capi.douyucdn.cn']
    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [url + str(offset)]

    # {
    #     "errorcode": 0,
    #     "data":[
    #         {
    #             vertical_src: "https://rpic.douyucdn.cn/live-cover/appCovers/2018/08/04/5230270_20180804114020_big.jpg",
    #             nickname: "早安酱ii",
    #             anchor_city: "武汉市"
    #         },
    #     ]
    # }

    def parse(self, response):
        # response为json格式的数据
        # 先把响应转成python数据类型
        list = json.loads(response.text)["data"]
        # 如果list为空，说明爬取完毕
        # if len(list) == 0:
        if self.offset == 60:
            return
        for info in list:
            item = DouyuItem()
            item['img'] = info['vertical_src']
            item['name'] = info['nickname']
            item['city'] = info['anchor_city']
            yield item

        # 实现翻页功能
        self.offset += 20
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)