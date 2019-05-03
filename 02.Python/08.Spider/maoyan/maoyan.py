import urllib.request
import urllib.parse
import re
import csv


class MaoYanSpider:
    def __init__(self):
        self.baseurl = 'http://maoyan.com/board/4?offset='
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
        self.page = 1
        self.offset = 0

    # 下载页面
    def load_page(self, url):
        req = urllib.request.Request(url, headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode()
        self.parse_page(html)

    # 解析页面
    def parse_page(self, html):
        # p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?releasetime">(.*?)</p>', re.S)
        p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?主演：(.*?)</p>.*?releasetime">(.*?)</p>', re.S)
        r_list = p.findall(html)
        self.write_page(r_list)

    # 保存页面
    def write_page(self, r_list):
        for r_tuple in r_list:
            with open("top.csv", "a", newline='') as f: # 开头不空行
                # 创建写入对象
                writer = csv.writer(f)
                L = [i.strip() for i in r_tuple]
                # ["霸王别姬","张国荣","1994..."]
                writer.writerow(L)

    def main(self):
        self.load_page(self.baseurl)
        while True:
            c = input("是否继续(y/n)?")
            if c.strip().lower() == 'y':
                self.page += 1
                self.offset = (self.page - 1) * 10
                url = self.baseurl + str(self.offset)
                self.load_page(url)
            else:
                print("爬取结束，谢谢使用！")
                break


if __name__ == "__main__":
    spider = MaoYanSpider()
    spider.main()
