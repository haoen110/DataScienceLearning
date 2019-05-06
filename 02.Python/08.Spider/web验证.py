import re
import requests


class NoteSpider:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0"}
        self.url = "http://code.tarena.com.cn/"
        # self.proxies = {"http":"http://23213:密码@IP:端口"}
        # auth参数存储用户名和密码（必须用元组）
        self.auth = ("tarenacode", "code_2013")

    def get_parse_page(self):
        res = requests.get(self.url, headers=self.headers, auth=self.auth, timeout=3)
        html = res.text
        # print(html)
        p = re.compile('<a href=".*?>(.*?)</a>', re.S)
        r_list = p.findall(html)
        print(r_list)
        self.write_page(r_list)

    def write_page(self, r_list):
        print("开始写入文件")
        with open("notes.txt", 'a') as f:
            for r_str in r_list:
                f.write(r_str + "\n\n")
        print("写入成功")


if __name__ == "__main__":
    spider = NoteSpider()
    spider.get_parse_page()