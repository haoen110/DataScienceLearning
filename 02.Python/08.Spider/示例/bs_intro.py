from bs4 import BeautifulSoup

html = '<div id="text">哈哈</div>'

# 创建解析对象
soup = BeautifulSoup(html, 'lxml')
# 查找节点
r_list = soup.find_all(id="text")
print(r_list)
for r in r_list:
    print(r.get_text())

r_list = soup.find_all("div", attrs={'id': "text"})
print(r_list)

####################################
html = '''<div class="test">你好</div>
<div class="test">再见</div>
<div class="test2">
    <span>第二次</span>
</div>'''

# class为test的div的文本内容
soup = BeautifulSoup(html, 'lxml')
divs = soup.find_all("div", attrs={"class": "test"})
print(type(divs))
for div in divs:
    print(div.string)
    print(div.get_text())

# class为test2的div下的span中的文本内容
divs = soup.find_all("div", attrs={"class": "test2"})
for div in divs:
    print(div.span.string)