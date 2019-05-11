import requests
import csv
import json

# url写get到的url
url = "https://movie.douban.com/j/chart/top_list?"
headers = {"User-Agent": "Mozilla/5.0"}
num = input("请输入要爬取的数量：")
# params 是抓包抓到webform里的内容形成的字典
params = {
    "type": "11",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": num
}

res = requests.get(url, params=params, headers=headers)
# html为json格式的数组
html = res.text
print(html)
# 数组 -> python列表
html = json.loads(html)
# 用for循环遍历每一个电影信息{}
for film in html:
    name = film['title']
    score = film['rating'][0]
    #{"rating":["9.6","50"]}
    with open("douban.csv", "a", newline='') as f:
        writer = csv.writer(f)
        L = [name, score]
        writer.writerow(L)

