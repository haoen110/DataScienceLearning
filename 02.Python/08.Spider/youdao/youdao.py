import urllib.request
import urllib.parse
import json


# 请输入你要翻译的内容
key = input("请输入要翻译的内容：")
# 把提交的form表单数据转换为bytes数据类型
data = {'i':key,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':'15567713651723',
        'sign':'3eee1e0b9cbebd65a65007f497a9b33a',
        'ts':'1556771365172',
        'bv':'d1dc01b5ffc1e7dfd53e6ee3c347fc81',
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTlME'
        }
# 字符串i=key&from=AUTO&to=AUTO&s....
data = urllib.parse.urlencode(data)
data = bytes(data, "utf-8")
# 发请求，获取相应
# url为POST地址，抓包工具抓到的
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
# 此处data为form表单数据，为bytes数据类型
req = urllib.request.Request(url, data=data, headers=headers)
res = urllib.request.urlopen(req)
r_json = res.read().decode("utf-8")

r_dict = json.loads(r_json)
print(r_dict["translateResult"][0][0]["tgt"])

