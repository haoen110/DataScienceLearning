import urllib.request
import urllib.parse


# 拼接URL
baseurl = "http://www.baidu.com/s?"
key = input("请输入要搜索的内容：")
# 进行urlencode()编码
key = urllib.parse.urlencode({"wd":key})
url = baseurl + key

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}

# 创建请求对象
req = urllib.request.Request(url, headers=headers)

# 获取响应对象
res = urllib.request.urlopen(req)
html = res.read().decode("utf-8")

# 写入文件
with open("搜索.html", "w", encoding='utf-8') as f:
    f.write(html)

