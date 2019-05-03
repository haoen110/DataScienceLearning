import urllib.request
import urllib.parse
import re


class NeiHanSpider:
    def __init__(self):
        self.baseurl = "https://www.neihanba.com/dz/"
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
        self.page = 1

    # 下载页面
    def load_page(self, url):
        req = urllib.request.Request(url, headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("gbk")
        self.parse_page(html)

    # 解析页面
    def parse_page(self, html):
        p = re.compile('<h4> <a href=.*?<b>(.*?)</b>.*?f18 mb20">(.*?)</div>', re.S)
        r_list = p.findall(html)
        self.write_page(r_list)

    # 保存页面
    def write_page(self, r_list):
        for r_tuple in r_list:
            with open("dz.txt", "a") as f:
                f.write('\n' + r_tuple[0].strip() + '\n' + r_tuple[1].strip() + '\n')

    def main(self):
        self.load_page(self.baseurl)
        while True:
            c = input("是否继续(y/n)?")
            if c.strip().lower() == 'y':
                self.page += 1
                url = self.baseurl + "list_" + str(self.page) + ".html"
                self.load_page(url)
            else:
                print("爬取结束，谢谢使用！")

                break


if __name__ == "__main__":
    spider = NeiHanSpider()
    spider.main()
