import requests

url = "http://img1.gtimg.com/news/pics/hv1/171/170/1619/105318996.jpg"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}

res = requests.get(url, headers=headers)
html = res.content
with open("airbus.jpg", "wb") as f:
    f.write(html)

print("图片下载成功")
