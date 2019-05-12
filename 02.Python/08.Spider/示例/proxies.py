# 普通代理
import requests

url = "http://httpbin.org/get"
proxies = {'https':'https://117.90.252.244:9000'}
headers = {"Uesr-Agent":"Mozilla/5.0"}
res = requests.get(url, proxies, headers=headers)
print(res.status_code)
print(res.text)

# 私密代理
proxies = {"http":"http://309435365:szayclhp@123.206.119.108:21081"}

