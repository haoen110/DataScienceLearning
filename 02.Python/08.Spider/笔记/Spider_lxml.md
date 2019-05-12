
# xpath工具（解析）
- xpath
    - 在XML文档中查找信息的语言,同样适用于HTML文档的检索
- xpath辅助工具
    - Chrome插件 ：XPath Helper
        - 打开 ：Ctrl + Shift + X
        - 关闭 ：Ctrl + Shift + X
    - Firefox插件 ：XPath checker
    - XPath表达式编辑工具 ：XML quire

## xpath匹配规则
- 匹配演示
  1. 查找bookstore下所有节点：`/bookstore`
  2. 查找所有的book节点：`//book`
  3. 查找所有book下的title节点中,lang属性为"en"的节点
      - `//book/title[@lang="en"]`
  4. 查找bookstore下的第2个book节点下的title节点:
      - `/bookstore/book[2]/title/text()`
- 选取节点
  - / ：从根节点开始选取 
  - //：从整个文档中查找节点
      - `//price  、  /bookstore/book//price`
  - @ ：选取某个节点的属性
      - `//title[@lang="en"]`
- @的使用
  - 选取1个节点：`//title[@lang="en"]`
  - 选取N个节点：`//title[@lang]`
  - 选取节点的属性值：`//title/@lang`
      - `<a class=....,src="http://..."`
- 匹配多路径
  - 符号：`|`
  - 获取所有book节点下的 title节点和price节点
      - `//book/title | //book/price`
- 函数
  - `contains()`：匹配一个属性值中包含某些字符串的节点
      - `//title[contains(@lang,"e")]`
  - `text()`
      - `//title[contains(@lang,"e")]/text()`

## lxml库及xpath使用
### lxml库 ：HTML/XML解析库
- 安装 
    - `python -m pip install lxml`
    - `conda install lxml`
- 使用流程
    1. 导模块
        - `from lxml import etree`
    2. 利用lxml库的etree模块创建解析对象
        - `parseHtml = etree.HTML(html)`
    3. 解析对象调用xpath工具定位节点信息
        - `r_list = parseHtml.xpath('xpath表达式')`
>只要调用了xpath,结果一定是列表 
    4. 如何获取节点对象的内容
        - `节点对象.text`


```python
from lxml import etree

html = """<div class="wrapper">
	<i class="iconfont icon-back" id="back"></i>
	<a href="/" id="channel">新浪社会</a>
	<ul id="nav">
		<li><a href="http://domestic.firefox.sina.com/" title="国内">国内</a></li>
		<li><a href="http://world.firefox.sina.com/" title="国际">国际</a></li>
		<li><a href="http://mil.firefox.sina.com/" title="军事">军事</a></li>
		<li><a href="http://photo.firefox.sina.com/" title="图片">图片</a></li>
		<li><a href="http://society.firefox.sina.com/" title="社会">社会</a></li>
		<li><a href="http://ent.firefox.sina.com/" title="娱乐">娱乐</a></li>
		<li><a href="http://tech.firefox.sina.com/" title="科技">科技</a></li>
		<li><a href="http://sports.firefox.sina.com/" title="体育">体育</a></li>
		<li><a href="http://finance.firefox.sina.com/" title="财经">财经</a></li>
		<li><a href="http://auto.firefox.sina.com/" title="汽车">汽车</a></li>
	</ul>
	<i class="iconfont icon-liebiao" id="menu"></i>
</div>"""
# 构造解析对象
parseHtml = etree.HTML(html)
# 利用解析对象调用xpath匹配
r1 = parseHtml.xpath('//a/@href')
#print(r1)

# 获取 /
r2 = parseHtml.xpath('//a[@id="channel"]/@href')
#print(r2)

# 获取非 /
r3 = parseHtml.xpath('//ul[@id="nav"]//a/@href')
#print(r3)
# 获取所有 a 节点的文本内容
r4 = parseHtml.xpath('//a/text()')
#print(r4)
# 获取 图片、军事 ... 
r5 = parseHtml.xpath('//ul[@id="nav"]//a')
for i in r5:
    print(i.text)
```

### 案例1 ：抓取百度贴吧帖子里面所有的图片
- 目标：抓取指定贴吧所有图片
- 思路：
    - 获取贴吧主页URL,下一页：找URL规律
    - 获取1页中每个帖子的URL
    - 对每个帖子URL发请求,获取帖子里图片URL
    - 对图片URL发请求,以wb方式写入本地文件
- 步骤
    1. 获取贴吧主页URL
        - `http://tieba.baidu.com/f? + 查询参数`
    2. 找到页面中所有帖子的URL
        - src : 完整链接
        - href : 和主URL进行拼接
            - /p/5926064184
            - http://tieba.baidu.com/p/5926064184
        - xpath匹配链接：
            - 写法1：`//div[@class="col2_right j_threadlist_li_right"]/div/div/a/@href`

            - 写法2(推荐)：`//div[@class="t_con cleafix"]/div/div/div/a/@href`
    3. 找每个帖子中图片URL
        - Xpath匹配：`//img[@class="BDE_Image"]/@src`
    4. 代码实现


```python
'''百度贴吧图片抓取'''
import requests
from lxml import etree


class TiebaImageSpider:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.baseurl = 'https://tieba.baidu.com'
        self.pageurl = 'https://tieba.baidu.com/f?'

    # 获取所有帖子URL列表
    def get_page_url(self, params):
        res = requests.get(self.pageurl, params=params, headers=self.headers)
        res.encoding = 'utf-8'
        print(res.url)
        html = res.text
        parse_html = etree.HTML(html)
        t_list = parse_html.xpath('//div[contains(@class,"t_con")]/div/div/div/a/@href')
        print(t_list)
        for t_link in t_list:
            t_link = self.baseurl + t_link
            self.get_image_url(t_link)

    # 获取帖子中图片URL列表
    def get_image_url(self, t_link):
        res = requests.get(t_link, headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        parse_html = etree.HTML(html)
        img_list = parse_html.xpath('//img[@class="BDE_Image"]/@src')
        for img_link in img_list:
            self.write_image(img_link)

    # 保存到本地
    def write_image(self, img_link):
        res = requests.get(img_link, headers=self.headers)
        res.encoding = 'utf-8'
        html = res.content
        filename = img_link[-12:]
        with open(filename, 'wb') as f:
            f.write(html)
            print("%s下载成功" % filename)

    # 主函数
    def main(self):
        name = input("请输入贴吧名字：")
        begin = int(input("请输入起始页："))
        end = int(input("请输入中止页："))
        for n in range(begin, end + 1):
            pn = (n - 1) * 50
            params = {'kw': name,
                      'pn': str(pn)}
            self.get_page_url(params)

# s = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
# s = '//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a/@href'
# s2 = '//cc/div/img[@class="BDE_Image"]/@src'


if __name__ == '__main__':
    spider = TiebaImageSpider()
    spider.main()
```

### 案例2：糗事百科-xpath
- 目标 ：用户昵称、段子内容、好笑数、评论数
- 步骤
    - 找URL
        - `https://www.qiushibaike.com/8hr/page/1/`
    - xpath匹配
        - 基准xpath：`//li[contains(@id,"qiushi")]`
            - 标题内容：``
            - 用户昵称：`.//span[@class="recmd-name"]`
            - 好笑数量：`./div/div/div/span[1]`
            - 评论数量：`./div/div/div/span[4]`


```python
import requests
from lxml import etree
import pymongo


class QiuShiSpider:
    def __init__(self):
        self.url = "https://www.qiushibaike.com/"
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.conn = pymongo.MongoClient("localhost", 27017)
        self.db = self.conn.spiderdb
        self.set = self.db.qiushi

    def get_page(self):
        res = requests.get(self.url, headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        self.parse_page(html)

    def parse_page(self, html):
        parse_html = etree.HTML(html)
        # 匹配每个段子列表
        base_list = parse_html.xpath('//li[contains(@id,"qiushi")]')
        # 遍历每个段子的借点对象
        for base in base_list:
            # 标题
            title = base.xpath('./div/a')[0].text
            # 用户昵称
            username = base.xpath('.//span[@class="recmd-name"]')[0].text
            # 好笑数量
            try:
                laugh_num = base.xpath('./div/div/div/span[1]')[0].text
                # 或：laugh_num = base.xpath('./div/div/div/span')[0].text
            except IndexError:
                laugh_num = 0
            # 评论数量
            try:
                com_num = base.xpath('./div/div/div/span[4]')[0].text
                # com_num = base.xpath('./div/div/div/span')[3].text
            except IndexError:
                com_num = 0

            d = {
                "title": title,
                "username": username,
                "laugh_num": laugh_num,
                "com_num": com_num
            }
            self.set.insert(d)
            print("存入数据库成功！")


if __name__ == "__main__":
    spider = QiuShiSpider()
    spider.get_page()

```
