# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomuItem(scrapy.Item):
    # 书名
    book = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 章节名称
    chapter = scrapy.Field()
    # 章节数
    chapter_num = scrapy.Field()
    # 章节链接
    chapter_url = scrapy.Field()

