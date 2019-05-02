import urllib.request
import urllib.parse
import random
import time


# 读取页面
def read_page(url):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode("utf-8")
    return html


# 写如文件
def write_page(filename, html):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)


# 主函数
def work():
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
        url = "http://tieba.baidu.com/f?" + kw + "&pn" + str(pn)
        html = read_page(url)
        filename = "第" + str(i) + "页.html"
        write_page(filename, html)
        print("第%d页爬取成功" % i)


if __name__ == "__main__":
    work()