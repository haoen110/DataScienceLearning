
# 解析
---
### 数据的分类
- 结构化数据
    - 有固定的格式，如 ：HTML、XML、JSON
- 非结构化数据
    - 图片、音频、视频，这类数据一般都存储为二进制
    
# 正则表达式 re
---
- 使用流程
    1. 创建编译对象：p = re.compile("正则表达式")
    2. 对字符串匹配：r = p.match("字符串")
    3. 获取匹配结果：print(r.group())
    
    
- 常用方法
    1. match(s) ：字符串开头的第1个,返回对象
    2. search(s)：从开始往后找,匹配第1个,返回对象
    3. group()  ：从match或search返回对象中取值
    4. findall()：所有全部匹配,返回一个列表
    
    
- 表达式
        - .  匹配任意字符(不能匹配\n)
        - \d 数字
        - \s 空白字符
        - \S 非空白字符  
        - [...] 包含[]内容 ：A[BCD]E  --> ABE  ACE  ADE 
        - \w 字母、数字、_
        
        - *  0次或多次
        - ?  0次或1次
        - +  1次或多次
        - {m} m次
        - {m,n} m-n次  AB{1,3}C --> ABC ABBC ABBBC
        
        - 贪婪匹配(.*) ：在整个表达式匹配成功的前提下,尽可能多的匹配*
        - 非贪婪匹配(.*?) ：在整个表达式匹配成功的前提下,尽可能少的匹配*
        
        - 分组


```python
# 贪婪匹配和非贪婪匹配
import re

s = """<div><p>春眠不觉晓，处处闻啼鸟</div></p>
<div><p>举头望明月，低头思故乡</div></p>"""

# 创建编译对象
p = re.compile('<div><p>.*</div></p>', re.S) # re.S：使.能够匹配\n在内的所有字符，相当于在中间/s/S
p2 = re.compile('<div><p>.*?</div></p>', re.S)
# 匹配字符串s
r = p.findall(s)
r2 = p2.findall(s)
print("贪婪匹配：", r)
print("非贪婪匹配：", r2)
```

    贪婪匹配： ['<div><p>春眠不觉晓，处处闻啼鸟</div></p>\n<div><p>举头望明月，低头思故乡</div></p>']
    非贪婪匹配： ['<div><p>春眠不觉晓，处处闻啼鸟</div></p>', '<div><p>举头望明月，低头思故乡</div></p>']



```python
# findall()分组示例
# 解释：先按照整体匹配出来，然后再匹配()中的，如果有两个或者多个括号，则以元祖的方式显示
import re

s = "A B C D"
p1 = re.compile("\w+\s+\w+")
print(p1.findall(s))

p2 = re.compile("(\w+)\s+\w+")
# 第一步：['A B', 'C D']
# 第二步：在A B，C D中匹配括号中的内容
print(p2.findall(s))

p3 = re.compile("(\w+)\s+(\w+)")
print(p3.findall(s))
```

    ['A B', 'C D']
    ['A', 'C']
    [('A', 'B'), ('C', 'D')]



```python
# 练习
# 打印：
# [("Tiger", "Two tiger..."), ("Rabbit", "Small Ra...")]
# 动物名称：Tiger
# 动物描述：....

import re

s = """\
<div class="animal">
  <p class="name">
    <a title="Tiger"></a>
  </p>

  <p class="contents">
    Two tigers two tigers run fast
  </p>
</div>

<div class="animal">
  <p class="name">
    <a title="Rabbit"></a>
  </p>

  <p class="contents">
    Small white rabbit white and white 
  </p>
</div>
"""

p = re.compile(r'<div class.*?title="(.*?)">.*?contents">(.*?)</p>', re.S)
r = p.findall(s)
print(r)
for animal in r:
    print("动物名称：", animal[0].strip())
    print("动物描述：", animal[1].strip())
```

    [('Tiger', '\n    Two tigers two tigers run fast\n  '), ('Rabbit', '\n    Small white rabbit white and white \n  ')]
    动物名称： Tiger
    动物描述： Two tigers two tigers run fast
    动物名称： Rabbit
    动物描述： Small white rabbit white and white


## 案例1：内涵段子脑筋急转弯抓取
- 网址 ：www.neihan8.com
- 步骤：
    1. 找URL规律
        - 第1页:https://www.neihanba.com/dz/
        - 第2页:https://www.neihanba.com/dz/list_2.html
        - 第3页:https://www.neihanba.com/dz/list_3.html
    2. 用正则匹配题目、内容
        - `p = re.compile('<h4> <a href=.*?<b>(.*?)</b>.*?f18 mb20">(.*?)</div>', re.S)`
    3. 写代码
        - 发请求
        - 用正则匹配
        - 写入本地文件


```python
import urllib.request
import urllib.parse
import re


class NeiHanSpider:
    def __init__(self):
        self.baseurl = "https://www.neihanba.com/dz/"
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
        self.page = 1

    # 下载页面
    def load_page(self, url):
        req = urllib.request.Request(url, headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("gbk")
        self.parse_page(html)

    # 解析页面
    def parse_page(self, html):
        p = re.compile('<h4> <a href=.*?<b>(.*?)</b>.*?f18 mb20">(.*?)</div>', re.S)
        r_list = p.findall(html)
        self.write_page(r_list)

    # 保存页面
    def write_page(self, r_list):
        for r_tuple in r_list:
            with open("dz.txt", "a") as f:
                f.write('\n' + r_tuple[0].strip() + '\n' + r_tuple[1].strip() + '\n')

    def main(self):
        self.load_page(self.baseurl)
        while True:
            c = input("是否继续(y/n)?")
            if c.strip().lower() == 'y':
                self.page += 1
                url = self.baseurl + "list_" + str(self.page) + ".html"
                self.load_page(url)
            else:
                print("爬取结束，谢谢使用！")

                break


if __name__ == "__main__":
    spider = NeiHanSpider()
    spider.main()
```

## 案例2：猫眼电影top100榜单,存到csv表格文件中
- 网址：猫眼电影 - 榜单 - top100榜
- 目标：抓取电影名、主演、上映时间
- 知识点讲解
    - csv模块的使用流程
        - 打开csv文件
            - `with open("测试.csv","a") as f:`
        - 初始化写入对象
            - `writer = csv.writer(f)`
        - 写入数据
            - `writer.writerow(列表)`
    - 示例 见05_csv示例.py
        1. 找URL
            - 第1页：http://maoyan.com/board/4?offset=0
            - 第2页：http://maoyan.com/board/4?offset=10
            - 第n页：offset = (n-1)*10
        2. 正则匹配
            - `<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?releasetime">(.*?)</p>`
        3. 写代码


```python
import urllib.request
import urllib.parse
import re
import csv


class MaoYanSpider:
    def __init__(self):
        self.baseurl = 'http://maoyan.com/board/4?offset='
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
        self.page = 1
        self.offset = 0

    # 下载页面
    def load_page(self, url):
        req = urllib.request.Request(url, headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode()
        self.parse_page(html)

    # 解析页面
    def parse_page(self, html):
        # p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?releasetime">(.*?)</p>', re.S)
        p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?主演：(.*?)</p>.*?releasetime">(.*?)</p>', re.S)
        r_list = p.findall(html)
        self.write_page(r_list)

    # 保存页面
    def write_page(self, r_list):
        for r_tuple in r_list:
            with open("top.csv", "a", newline='') as f: # 开头不空行
                # 创建写入对象
                writer = csv.writer(f)
                L = [i.strip() for i in r_tuple]
                # ["霸王别姬","张国荣","1994..."]
                writer.writerow(L)

    def main(self):
        self.load_page(self.baseurl)
        while True:
            c = input("是否继续(y/n)?")
            if c.strip().lower() == 'y':
                self.page += 1
                self.offset = (self.page - 1) * 10
                url = self.baseurl + str(self.offset)
                self.load_page(url)
            else:
                print("爬取结束，谢谢使用！")
                break


if __name__ == "__main__":
    spider = MaoYanSpider()
    spider.main()
```

# Fiddler常用菜单
1. Inspector：查看抓到的数据包的详细内容
    - 分为请求(request)和响应(response)两部分
2. 常用选项
    - Headers：显示客户端发送到服务器的header,包含客户端信息、cookie、传输状态
    - WebForms：显示请求的POST数据 <body>
    - Raw：将整个请求显示为纯文本
3. 请求方式及案例
    - GET
    - POST
    - Cookie模拟登陆


## 什么是cookie、session
- HTTP是一种无连接协议,客户端和服务器交互仅仅限于请求/响应过程,结束后断开,下一次请求时,服务器会认为是一个新的客户端,为了维护他们之间的连接,让服务器知道这是前一个用户发起的请求,必须在一个地方保存客户端信息。
    - cookie：通过在客户端记录的信息确定用户身份
    - session：通过在服务端记录的信息确定用户身份

## 案例3：使用cookie模拟登陆cnblogs
    1. 通过抓包工具、F12获取到cookie(先登陆1次网站)
	2. 正常发请求
	url：https://home.cnblogs.com/u/haoenwei/
