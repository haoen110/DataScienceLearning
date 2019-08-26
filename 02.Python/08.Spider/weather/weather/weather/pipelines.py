# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WeatherPipeline(object):
    def process_item(self, item, spider):
        print("=========================")
        # print(item["day"])
        print(item["tm"])
        print(item["temperature"])
        print(item["dew_point"])
        print(item["humidity"])
        print(item["wind"])
        print(item["wind_speed"])
        print(item["pressure"])
        print("=========================")
