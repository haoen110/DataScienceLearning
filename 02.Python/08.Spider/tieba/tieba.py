import urllib.request
import urllib.parse
import random
import time

header_list = [{"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"},
               {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"},
               {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}]
headers = random.choice(header_list)

# 主体程序
name = input("请输入贴吧名：")
begin = int(input("请输入起始页："))
end = int(input("请输入中止页："))

# 对贴吧名字name编码
kw = {"kw":name}
kw = urllib.parse.urlencode(kw)

# 拼接URL，发请求，获取相应
for i in range(begin, end+1):
    # 拼接URL
    pn = (i-1)*50
    url = "http://tieba.baidu.com/f?" + kw + "&pn" + str(pn)
    # 发请求
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req, timeout=5)  # 可以设置超时
    time.sleep(1)
    html = res.read().decode("utf-8")

    # 写入文件
    filename = "第" + str(i) + "页.html"
    with open(filename, "w", encoding="utf-8") as f:
        print("正在爬取第%d页" % i)
        f.write(html)
        print("第%d页爬取成功" % i)
        print("*" * 30)