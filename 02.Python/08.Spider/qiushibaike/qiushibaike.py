import requests
from lxml import etree
import pymongo


class QiuShiSpider:
    def __init__(self):
        self.url = "https://www.qiushibaike.com/"
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.conn = pymongo.MongoClient("localhost", 27017)
        self.db = self.conn.spiderdb
        self.set = self.db.qiushi

    def get_page(self):
        res = requests.get(self.url, headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        self.parse_page(html)

    def parse_page(self, html):
        parse_html = etree.HTML(html)
        # 匹配每个段子列表
        base_list = parse_html.xpath('//li[contains(@id,"qiushi")]')
        print(base_list)
        # 遍历每个段子的借点对象
        # for base in base_list:
        #     # 标题
        #     title = base.xpath('./div/a')[0].text
        #     # 用户昵称
        #     username = base.xpath('.//span[@class="recmd-name"]')[0].text
        #     # 好笑数量
        #     try:
        #         laugh_num = base.xpath('./div/div/div/span[1]')[0].text
        #         # 或：laugh_num = base.xpath('./div/div/div/span')[0].text
        #     except IndexError:
        #         laugh_num = 0
        #     # 评论数量
        #     try:
        #         com_num = base.xpath('./div/div/div/span[4]')[0].text
        #         # com_num = base.xpath('./div/div/div/span')[3].text
        #     except IndexError:
        #         com_num = 0
        #
        #     d = {
        #         "title": title,
        #         "username": username,
        #         "laugh_num": laugh_num,
        #         "com_num": com_num
        #     }
        #     self.set.insert(d)
        #     print("存入数据库成功！")


if __name__ == "__main__":
    spider = QiuShiSpider()
    spider.get_page()
