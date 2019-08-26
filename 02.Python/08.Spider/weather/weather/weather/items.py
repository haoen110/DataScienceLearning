# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # day = scrapy.Field()
    tm = scrapy.Field()
    temperature = scrapy.Field()
    dew_point = scrapy.Field()
    humidity = scrapy.Field()
    wind = scrapy.Field()
    wind_speed = scrapy.Field()
    pressure = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()

