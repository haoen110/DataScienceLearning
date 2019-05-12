import requests
from bs4 import BeautifulSoup

url = "https://www.qiushibaike.com/"
headers = {"User-Agent": "Mozilla/5.0"}

res = requests.get(url, headers=headers)
res.encoding = 'utf-8'
html = res.text

soup = BeautifulSoup(html, 'lxml')
r_list = soup.find_all("div", attrs={"class": "recommend-article"})

for r in r_list:
    print(r.ul.li.div.a)
    print("*" * 30)
