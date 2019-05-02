import urllib.request
import urllib.parse


class TiebaSpider():
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
        self.baseurl = "http://tieba.baidu.com/f?"

    def read_page(self, url):
        req = urllib.request.Request(url, headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        return html

    def write_page(self, filename, html):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)

    def work(self):
        name = input("请输入贴吧名：")
        begin = int(input("请输入起始页："))
        end = int(input("请输入中止页："))

        # 对贴吧名字name编码
        kw = {"kw": name}
        kw = urllib.parse.urlencode(kw)

        # 拼接URL，发请求，获取相应
        for i in range(begin, end + 1):
            # 拼接URL
            pn = (i - 1) * 50
            url = self.baseurl + kw + "&pn" + str(pn)
            html = self.read_page(url)
            filename = "第" + str(i) + "页.html"
            self.write_page(filename, html)
            print("第%d页爬取成功" % i)


if __name__ == "__main__":
    spider = TiebaSpider()
    spider.work()