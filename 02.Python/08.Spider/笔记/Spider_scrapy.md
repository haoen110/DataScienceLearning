
# 多线程爬虫

### 进程线程回顾

- 进程
    - 系统中正在运行的一个应用程序
    - 1个CPU核心1次只能执行1个进程,其他进程处于非运行状态
    - N个CPU核心可同时执行N个任务
- 线程
    - 进程中包含的执行单元,1个进程可包含多个线程
    - 线程可使用所属进程空间(1次只能执行1个线程,阻塞)
    - 锁：防止多个线程同时使用共享空间
- GIL：全局解释锁
    - 执行通行证,仅此1个,拿到了通行证可执行,否则等
- 应用场景
    - 多进程：大量的密集的计算
    - 多线程：I/O密集
        - 爬虫：网络I/O
	- 写文件：本次磁盘I/O

### 案例：使用多线程爬取 百思不得其姐 段子
- 爬取目标 ：段子内容
- URL ：http://www.budejie.com/
- xpath表达式 
    - `//div[@class="j-r-list-c-desc"]/a/text()`
- 知识点
    - 队列(from queue import Queue)
        - `put()`
        - `get()`
        - `Queue.empty()`：是否为空
        - `Queue.join()`：如果队列为空,执行其他程序
    - 线程(import threading)
        - `threading.Thread(target=...)`


```python
import requests
from lxml import etree
from queue import Queue
import threading
import time


class BsSpider:
    def __init__(self):
        self.baseurl = "http://www.budejie.com/"
        self.headers = {"User_Agent": "Mozilla/5.0"}
        self.urlQueue = Queue()  # url队列
        self.resQueue = Queue()  # 响应队列

    # 生成URL队列
    def get_url(self):
        for num in range(1, 51):
            url = self.baseurl + str(num)  # 1是第一页
            self.urlQueue.put(url)

    # 响应队列
    def get_html(self):
        while True:
            url = self.urlQueue.get()
            res = requests.get(url, headers=self.headers)
            res.encoding = 'utf-8'
            html = res.text
            # 放到响应队列
            self.resQueue.put(html)
            # 清除此任务
            self.urlQueue.task_done()

    # 解析页面
    def get_content(self):
        while True:
            # 从响应队列中一次获取html源码
            html = self.resQueue.get()
            parse_html = etree.HTML(html)
            r_list = parse_html.xpath('//div[@class="j-r-list-c-desc"]/a/text()')
            for r in r_list:
                print(r + "\n")
            # 清除任务
            self.resQueue.task_done()

    def main(self):
        # 存放所有的线程
        thread_list = []
        # 获取url队列
        self.get_url()
        # 创建getpage线程
        for i in range(3):
            thread_res = threading.Thread(target=self.get_html)
            thread_list.append(thread_res)
        for i in range(2):
            thread_parse = threading.Thread(target=self.get_content)
            thread_list.append(thread_parse)
        # 所有线程开始干活
        for th in thread_list:
            th.setDaemon(True)
            th.start()
        # 如果队列为空，则执行其他程序
        self.urlQueue.join()
        self.resQueue.join()
        print("运行结束")


if __name__ == '__main__':
    begin = time.time()
    spider = BsSpider()
    spider.main()
    end = time.time()
    print("运行时间：", end - begin)
```

## BeautifulSoup
- 定义
    - HTML或XML的解析器,依赖于lxml
- 安装：`python -m pip install beautifulsoup4`
- 导模块：`from bs4 import BeautifulSoup`
- 使用流程
    - 导入模块
        - `from bs4 import BeautifulSoup`
    - 创建解析对象 
        - `soup = BeautifulSoup(html,'lxml')`
    - 查找节点对象
        - `soup.find_all(name="属性值")`
        
### 支持的解析库
- lxml：BeautifulSoup(html,'lxml')
    - 速度快，文档容错能力强
- python标准库：BeautifulSoup(html,'html.parser')
    - 速度一般
- xml解析器：BeautifulSoup(html,'xml')
    - 速度快，文档容错能力强
    
### 节点选择器
- 选择节点
    - `soup.节点名`：`soup.a、soup.ul`
- 获取文本内容
    - `soup.节点名.string`
- 常用方法：`find_all()`：返回列表
    - `r_list = soup.find_all(属性名="属性值")`
        - `r_list = soup.find_all(class="test")` # 报错尝试使用class_
    - `r_list=soup.find_all("节点名",attrs={"名":"值"})`
        - `r_list=soup.find_all("div",attrs={"class":"test"}`


```python
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
```

# Scrapy框架
###  解释
- 异步处理框架,可配置和可扩展程度非常高,Python中使用最广泛的爬虫框架

### 框架组成
- 引擎(Engine) ：整个框架核心
- 调度器(Scheduler) ：接受从引擎发过来的URL,入队列
- 下载器(Downloader)：下载网页源码,返回给爬虫程序
- 项目管道(Item Pipeline) ：数据处理
- 下载器中间件(Downloader Middlewares)
    - 处理引擎与下载器之间的请求与响应
- 蜘蛛中间件(Spider Middlerwares)
    - 处理爬虫程序输入响应和输出结果以及新的请求
- Item：定义爬取结果的数据结构,爬取的数据会被赋值为Item对象

### 运行流程
1. Engine开始统揽全局,向Spider索要URL
2. Engine拿到url后,给Scheduler入队列
3. Schduler从队列中拿出url给Engine,通过Downloader Middlewares给Downloader去下载
4. Downloader下载完成,把response给Engine
5. Engine把response通过Spider Middlewares给Spider
6. Spider处理完成后,
    - 把数据给Engine,交给Item Pipeline处理,
    - 把新的URL给Engine,重复2-6步
7. Scheduler中没有任何Requests请求后,程序结束

### Scrapy爬虫项目步骤
1. 新建项目
    - `scrapy startproject 项目名`
2. 明确目标(items.py)
3. 制作爬虫程序
    - cd XXX/spiders：`scrapy genspider 文件名 域名`
4. 处理数据(pipelines.py)
5. 配置settings.py
6. 运行爬虫项目
    - `scrapy crawl 爬虫名`

### scrapy项目文件详解
- 目录结构
        testspider/
        ├── scrapy.cfg   #项目基本配置文件,不用改
        └── testspider
            ├── __init__.py
            ├── items.py       # 定义爬取数据的结构
            ├── middlewares.py # 下载器中间件和蜘蛛中间件实现
            ├── pipelines.py   # 处理数据
            ├── settings.py    # 项目全局配置
            └── spiders        # 存放爬虫程序
                ├── __init__.py
                ├── myspider.py
                
### settings.py配置
      # 是否遵守robots协议,该为False
      ROBOTSTXT_OBEY = False

      # 最大并发量,默认为16个
      CONCURRENT_REQUESTS = 32

      # 下载延迟时间为3秒
      DOWNLOAD_DELAY = 3

      # 请求报头
      DEFAULT_REQUEST_HEADERS = {
        'User-Agent': "Mozilla/5.0",
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Accept-Language': 'en',
        }

      # 蜘蛛中间件
      SPIDER_MIDDLEWARES = {
         'testspider.middlewares.TestspiderSpiderMiddleware': 543,
        }

      # 下载器中间件
      DOWNLOADER_MIDDLEWARES = {
         'testspider.middlewares.TestspiderDownloaderMiddleware': 543,
        }

      # 管道文件
      ITEM_PIPELINES = {
         'testspider.pipelines.TestspiderPipeline': 300,
        }

### 案例：抓取百度首页源码,存到baidu.html中
1. `scrapy startproject baidu`
2. `cd baidu/baidu`
3. `subl items.py(此示例可不用操作)`
4. `cd spiders`
5. `scrapy genspider baiduspider baidu.com`
        #爬虫名
        #域名
        #start_urls
        def parse(self,response):
            with open("baidu.html","w") as f:
                f.write(response.text)
6. `subl settings.py`
    - 关闭robots协议
    - 添加Headers
7. `cd spiders`
8. `scrapy crawl baiduspider`

>### pycharm运行scrapy项目
1. 创建文件begin.py和scrapy.cfg同目录
        from scrapy import cmdline
        cmdline.execute("scrapy crawl baiduspider".split())
2. Editconfigurations -> + -> python
        name : spider
        Script : begin.py的路径
        working directory : 你自己的项目路径
3. 点击运行

>#### 生成器
1. yield作用 ：把一个函数当做一个生成器使用
2. 斐波那契数列 Fib.py
3. yield特点 ：让函数暂停,等待下1次调用


```python
# Fib.py
def fib(n):
    a, b, s = 0, 1, 0
    while s < n:
        a, b = b, a + b
        s += 1
        yield b

print(fib(5).__next__())
for i in fib(10):
    print(i)
```

    1
    1
    2
    3
    5
    8
    13
    21
    34
    55
    89


### 项目：csdn 
1. 知识点 yield 、pipelines.py
2. 目标
    - https://blog.csdn.net/qq_42231391/article/details/83506181
    - 标题、发表时间、阅读数
    - 步骤
        - 创建项目
        - 定义数据结构(items.py)
        - 创建爬虫程序
        - 第3步抓取的数据通过项目管道去处理
        - 全局配置
        - 运行爬虫程序

### 项目：Daomu
1. URL ：http://www.daomubiji.com/dao-mu-bi-ji-1
2. 目标
    - 书名、书的标题、章节名称、章节数量、章节链接
3. 步骤
    - 创建项目 Daomu
    - 改items.py(定义数据结构)
    - 创建爬虫文件
    - 改pipelines.py(项目管道文件)
    - 配置settings.py
    - 运行爬虫

>#### 知识点
- `extract()`：获取选择器对象中的文本内容
    - `response.xpath('.../text()')` 得到选择器对象(节点文本) `[<selector ...,data='文本内容'>]`
    - `extract()` 把选择器对象中的文本取出来 `['文本内容']`
- 爬虫程序中的 start_urls必须为列表
    - `start_urls = []`
- pipelines.py中必须有1个函数叫
    - `process_item(self,item,spider)`，当然还可以写任何其他函数

>#### 存入MongoDB数据库
- 在settings.py中定义相关变量
    - `MONGODB_HOST = `
    - `MONGODB_PORT = `
- 可在pipelines.py中新建一个class
        from Daomu import settings
        class DaomumongoPipeline(object):
            def __init__(self):
            host = settings.MONGODB_HOST
- 在settings.py文件中设置你的项目管道
        ITEM_PIPELINES = {
          "Daomu.pipelines.DaomumongoPipeline":100,
          }
#### 存入MySQL数据库
- `self.db.commit()`
- `Csdn项目存到mongodb和mysql`

### 腾讯招聘网站案例
- URL
    - 第1页：`https://careers.tencent.com/search.html?index=1`
    - 第2页：`https://careers.tencent.com/search.html?index=2`
- Xpath匹配
    - 基准xpath表达式(每个职位节点对象)
    - `//div[@class="search-content"]`
        - 职位名称：`.//h4/text()`
        - 工作地点：`.//span[2]/text()`
        - 职位类别：`.//span[3]/text()`
        - 发布时间：`.//span[4]/text()`
        - 详情信息：`.//p[2]/text()`

### 设置手机抓包
    - Fiddler(设置抓包)
    - 在手机上安装证书
        - 手机浏览器打开：http://IP地址:8888 (IP地址是你电脑的IP,8888是Fiddler设置的端口)
        - 在页面上下载(FiddlerRoot certificate)
        - 下载文件名：FiddlerRoot.cer
        0 直接安装
    - 设置代理
        - 打开手机上已连接的无线, 代理设置 -> 改成 手动
        - IP地址：你电脑的IP (ipconfig / ifconfig)
        - 端口号：8888

## 如何设置随机User-Agent
1. settings.py(少量User-Agent切换,不推荐)
    - 定义USER_AGENT变量值
    - `DEFAULT_REQUEST_HEADER={"User-Agent":"",}`
    
    
2. 设置中间件的方法来实现
    - 项目目录中新建user_agents.py，放大量Agent
    - `user_agents = ['','','','','']`
    - middlewares.py写类:
            from 项目名.user_agents import user_agents
            import random
            class RandomUserAgentMiddleware(object):
                def process_request(self,request,spider):
                    request.headers["User-Agent"] = random.choice(user_agents)
    - 设置settings.py
            DOWNLOADER_MIDDLEWARES = {"项目名.middlewares.RandomUserAgentMiddleware" : 1}
            
            
3. 直接在middlewares.py中添加类
        class RandomUserAgentMiddleware(object):
            def __init__(self):
                self.user_agents = ['','','','','','']
            def process_request(self,request,spider):
                request.header['User-Agent'] = random.choice(self.user_agents)

## 设置代理(DOWNLOADER MIDDLEWARES)
- middlewares.py中添加代理中间件ProxyMiddleware
        class ProxyMiddleware(object):
            def process_request(self,request,spider):
                request.meta['proxy'] = "http://180.167.162.166:8080"
- settings.py中添加
        DOWNLOADER_MIDDLEWARES = {
           'Tengxun.middlewares.RandomUserAgentMiddleware': 543,
           'Tengxun.middlewares.ProxyMiddleware' : 250,
        }

## 图片管道 ：ImagePipeline
- 使用流程(要操作的文件)
    1. settings.py
        - 设置图片要保存的路径的变量
        - IMAGES_STORE = "/home/tarena/aaa/aaa/images"
    2. pipelines.py
        - 导入scrapy定义好的图片管道类
        - `from scrapy.pipelines.images import ImagesPipeline`
    3. 定义自己的class,继承scrapy的图片管道类
            class AAAImagePipeline(ImagesPipeline):
            def get_media_requests(self,item,info):
                ... ... 

### 案例 ：斗鱼图片抓取案例(手机app)
- 菜单 --> 颜值
    - `http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=0`
- 抓取目标
    - 图片链接
    - 主播名
    - 城市
    - 把所有图片保存在 IMAGES_STORE
- 步骤
    1. 前提 ：手机和电脑一个局域网
    2. Fiddler抓包工具
        Connections : Allow remote computers to ..
        HTTPS : ...from all processes
    3. IP地址 ：Win+r -> cmd -> ipconfig
    4. 配置手机
        - 手机浏览器 ：http://IP:8888
        - 下载 FiddlerRoot certificate
    5. 安装
        - 设置 -> 更多 -> ... -> 从存储设备安装
    6. 设置手机代理
        - 长按 wifi,->代理
        - IP地址 ：
        - 端口号 ：

>dont_filter参数

      scrapy.Request(url,callback=...,dont_filter=False)
      dont_filter参数 ：False->自动对URL进行去重
                        True -> 不会对URL进行去重

### scrapy对接selenium+phantomjs
1. 创建项目 ：Jd
2. middlewares.py中添加selenium
    - 导模块 ：from selenium import webdriver
    - 定义中间件
          class seleniumMiddleware(object):
               ... 
           def process_request(self,request,info):
               # 注意：参数为request的url
               self.driver.get(request.url)
3. settings.py
    - `DOWNLOADER_MIDDLEWARES={"Jd.middleware.seleniumMiddleware":20}`

### Scrapy模拟登陆
- 创建项目 ：cnblog
- 创建爬虫文件

## 机器视觉与tesseract
- OCR(Optical Character Recognition)光学字符识别
    - 扫描字符 ：通过字符形状 --> 电子文本,OCR有很多的底层识别库
- tesseract(谷歌维护的OCR识别开源库,不能import,工具)
    1. 安装 
        - windows下载安装包
            - `https://sourceforge.net/projects/tesseract-ocr-alt/files/tesseract-ocr-setup-3.02.02.exe/download`
            - 安装完成后添加到环境变量
        - Ubuntu : `suo apt-get install tesseract-ocr`
        - Mac    : `brew install tesseract`
    2. 验证
        - 终端 ：tesseract test1.jpg text1.txt
    3. 安装pytesseract模块
        - `python -m pip install pytesseract`
        - 方法很少,就用1个,图片转字符串：image_to_sting
- Python图片的标准库
    - `from PIL import Image`

### 示例
1. 验证码图片以wb方式写入到本地
2. image = Image.open("验证码.jpg")
3. s = pytesseract.image_to_string(image)

## 分布式介绍
- 条件
    1. 多台服务器(数据中心、云服务器)
    2. 网络带宽
- 分布式爬虫方式
    1. 主从分布式
        - 主机分配子机的目标url
    2. 对等分布式
- scrapy-redis
