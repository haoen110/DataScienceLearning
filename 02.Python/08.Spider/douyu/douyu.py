# 能点：<li title="下一页" class=" dy-Pagination-next" aria-disabled="false" tabindex="0"><span class="dy-Pagination-item-custom">下一页</span></li>
# 不能点：<li title="下一页" class="dy-Pagination-disabled dy-Pagination-next" aria-disabled="true"><span class="dy-Pagination-item-custom">下一页</span></li>
# 基路径：//li
# 直播间：".//h3[@class="DyListCover-intro"]"
# 直播区：".//span[@class="DyListCover-zone"]"
# 热度：".//span[@class="DyListCover-hot"]"
# 主播名："//li//h2/text()"

import time
from selenium import webdriver
from lxml import etree


class DouYu:
    def __init__(self):
        self.url = "https://www.douyu.com/directory/all"
        self.base_xpath = '//li'
        self.uname = './/h2/text()'
        self.zone = './/span[@class="DyListCover-zone"]'
        self.lname = './/h3[@class="DyListCover-intro"]'
        self.hot = './/span[@class="DyListCover-hot"]'

    def get_page(self):
        n = int(input("请输入要爬取的页数："))
        driver = webdriver.Chrome()
        driver.get(self.url)
        for i in range(n):
            parse_index = etree.HTML(driver.page_source)
            live = parse_index.xpath(self.base_xpath)
            print(live)
            for j in live:
                uname = j.xpath(self.uname)
                print(uname)


douyu = DouYu()
douyu.get_page()


