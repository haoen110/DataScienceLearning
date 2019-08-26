# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem


class WeatherSpider(scrapy.Spider):
    name = 'Weather'
    allowed_domains = ['wunderground.com']
    start_urls = ['https://www.wunderground.com/history/daily/cn/shenzhen/ZGSZ/date/2019-1-1']

    def parse(self, response):
        item = WeatherItem()
        r_list = response.xpath('//div[@class="observation-table"]//tbody/tr')
        for r in r_list:
            # item["day"] = str(2019) + '-' + str(1) + '-' + str(1)
            # Time
            item["tm"] = r.xpath('./td[1]/text()').extract()[0]
            # Temperature
            item["temperature"] = r.xpath('./td[2]').extract()[0]
            # dew point
            item["dew_point"] = r.xpath('./td[3]').extract()[0]
            # humidity
            item["humidity"] = r.xpath('./td[4]').extract()[0]
            # wind
            item["wind"] = r.xpath('./td[5]').extract()[0]
            # wind speed
            item["wind_speed"] = r.xpath('./td[6]').extract()[0]
            # pressure
            item["pressure"] = r.xpath('./td[8]').extract()[0]

            yield item
        # 不加/text()出现的是选择器对象且包含节点所有内容[<selector .., data ='<h1>...</h1>']
        # 若加/text()也是得到选择器对象（节点文本）[selector ..., data='文本']
        # extract将选择器对象中文本取出来['文本内容']