from lxml import etree

with open('test.txt') as f:
    html = f.read()

# 构造解析对象
parseHtml = etree.HTML(html)
# 利用解析对象调用xpath匹配
r1 = parseHtml.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
print(r1)