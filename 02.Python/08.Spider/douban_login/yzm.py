import requests
from lxml import etree
import pytesseract
from PIL import Image
from selenium import webdriver

url = "https://www.douban.com/"
headers = {"User-Agent":"Mozilla/5.0"}
# 先访问网站得到html
res = requests.get(url,headers=headers)
res.encoding = "utf-8"
html = res.text
# 用xpath把验证码图片的链接给拿出来
parseHtml = etree.HTML(html)
s = parseHtml.xpath('//img[@class="captcha_image"]/@src')[0]
# 访问验证码图片链接,得到html(字节流)
res = requests.get(s,headers=headers)
res.encoding = "utf-8"
html = res.content
# 把图片保存到本地
with open("zhanshen.jpg","wb") as f:
    f.write(html)
# 把图片->字符串
image = Image.open("test1.jpg")
s = pytesseract.image_to_string(image)
print(s)
# 把这个字符串输入到验证码框中
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_name("captcha-solution").send_keys(s)
driver.save_screenshot("验证码输入.png")

driver.quit()