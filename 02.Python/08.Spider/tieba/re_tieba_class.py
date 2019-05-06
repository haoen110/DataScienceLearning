import requests


class TiebaSpider():
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
        self.baseurl = "http://tieba.baidu.com/f?"

    def read_page(self, params):
        res = requests.get(self.baseurl, params=params, headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        return html

    def write_page(self, filename, html):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)

    def work(self):
        name = input("请输入贴吧名：")
        begin = int(input("请输入起始页："))
        end = int(input("请输入中止页："))

        # 对贴吧名字name编码
        params = {"kw": name}

        # 拼接URL，发请求，获取相应
        for i in range(begin, end + 1):
            # 拼接URL
            pn = (i - 1) * 50
            att = "&pn" + str(pn)
            params = {"kw": name + att}
            print(name + att)
            html = self.read_page(params)
            filename = "第" + str(i) + "页.html"
            self.write_page(filename, html)
            print("第%d页爬取成功" % i)


if __name__ == "__main__":
    spider = TiebaSpider()
    spider.work()