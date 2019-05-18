# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import scrapy

class DouyuPipeline(object):
    def process_item(self, item, spider):
        return item


class DouyuImagePipeline(ImagesPipeline):
    # 此方法名不能变
    def get_media_requests(self, item, info):
        # 1. 获取图片链接
        url = item['img']
        # 2. 想图片链接发请求，响应会保存在settings.py中的IMAGES_STORE
        yield scrapy.Request(url)

