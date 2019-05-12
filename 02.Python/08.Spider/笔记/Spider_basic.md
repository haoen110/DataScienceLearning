
# 网络爬虫
- 定义：网络蜘蛛、网络机器人,抓取网络数据的程序
- 总结：用Python程序去模仿人去访问网站,模仿的越逼真越好
- 目的：通过有效的大量数据分析市场走势、公司决策

### 企业获取数据的方式
1. 公司自有数据
2. 第三方数据平台购买
    - 数据堂、贵阳大数据交易所
3. 爬虫爬取数据
    - 市场上没有或者价格太高,利用爬虫程序爬取
    
### Python做爬虫优势
- 请求模块、解析模块丰富成熟,强大的scrapy框架
    - PHP：对多线程、异步支持不太好
    - JAVA：代码笨重,代码量很大
    - C/C++：虽然效率高,但是代码成型很慢
    
### 爬虫分类
1. 通用网络爬虫(搜索引擎引用,需要遵守robots协议)
    - http://www.taobao.com/robots.txt
    - 搜索引擎如何获取一个新网站的URL
        - 网站主动向搜索引擎提供(百度站长平台)
        - 和DNS服务网(万网),快速收录新网站
2. 聚焦网络爬虫
    - 自己写的爬虫程序：
        - 面向主题的爬虫
        - 面向需求的爬虫
        
### 爬取数据步骤
1. 确定需要爬取的URL地址
2. 通过HTTP/HTTPS协议来获取相应的HTML页面
3. 提取HTML页面有用的数据
    - 所需数据，保存
    - 页面中有其他的URL，继续第2步

# 工具    
### Anaconda和Spyder
1. Anaconda：开源的Python发行版本
2. Spyder：集成开发环境
    - Spyder常用快捷键：
    - 注释/取消注释：ctrl + 1
    - 保存：ctrl + s
    - 运行程序：f5
    - 自动补全：Tab
    
### Chrome浏览器插件
- 安装步骤
    1. 右上角 - 更多工具 - 扩展程序
    2. 点开右上角 - 开发者模式
    3. 把插件拖拽到浏览器页面，释放鼠标，点击添加扩展...
- 插件介绍
    1. Proxy SwitchOmega：代理切换插件
    2. Xpath Helper：网页数据解析插件
    3. JSON View：查看json格式的数据(好看)
    
### Fiddler抓包工具
1. mac安装
    - 安装mono
    - 执行 `/Library/Frameworks/Mono.framework/Versions/<Mono Version>/bin/mozroots --import --sync`
    - 执行 `export PATH="/Library/Frameworks/Mono.framework/Versions/5.20.1/bin:$PATH"`
2. 抓包工具设置
    - Tools -> options -> HTTPS -> ...from browers only
    - connections：设置端口号 8888
3. 设置浏览器代理
    - Proxy SwitchOmega -> 选项 -> 新建情景模式 -> HTTP 127.0.0.1 8888 -> 应用选项
4. 浏览器右上角图标 -> proxy(self) -> 访问百度

# 知识点
### WEB
- HTTP和HTTS
    - HTTP：80
    - HTTPS：443，HTTP的升级版，加了一个安全套接层
- GET和POST
    - GET：查询参数都会在URL上显示出来
    - POST：查询参数和需要提交数据是隐藏在Form表单里的，不会再URL地址上显示
- URL：统一资源定位符
    - https://  item.jd.com  :80   /26809408972.html #detail
    - 协议     域名/IP地址  端口  访问资源的路径    锚点
- User-Agent
    - 记录用户的浏览器、操作系统等，为了让用户获取更好的HTML页面效果
        - User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
        - Mozilla Firefox：(Gecko内核)
        - IE：Trident(自己的内核)
        - Linux：KTHML(like Gecko)
        - Apple：Webkit(like KHTML)
        - Google：Chrome(like Webkit)
        - 其他浏览器都是模仿IE/Chrome

### 爬虫请求模块
- 版本
    - python2：urllib2、urllib
    - python3：把urllib和urllib2合并,urllib.request
- 常用方法
    - `urllib.request.urlopen("网址")`
        - 作用：向网站发起一个请求并获取响应
        - 字节流 = `response.read()`
        - 字符串 = `response.read().decode("utf-8")`
            - encode() : 字符串 --> bytes
            - decode() : bytes  --> 字符串
    - 重构User-Agent
        - 不支持重构User-Agent：urlopen()
        - 支持重构User-Agent
            - urllib.request.Request(添加User-Agent)
            - urllib.request.Request("网址",headers="字典")
            - User-Agent是爬虫和反爬虫斗争的第一步,发送请求**必须**带User-Agent
            
#### 使用流程(见 02_urllib.request.Request.py)
1. 利用Request()方法构建请求对象
2. 利用urlopen()方法获取响应对象
    - 利用响应对象的read().decode("utf-8")获取内容
    - 响应对象response的方法
        1. read()：读取服务器响应的内容
        2. getcode()：返回HTTP的响应码
                print(respones.getcode())
                200 ：成功
                4XX ：服务器页面出错
                5XX ：服务器出错
        3. geturl()：返回实际数据的URL(防止重定向问题)


```python
import urllib.request

# 1. 创建请求对象（有User-Agent）
url = "http://www.baidu.com/"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}

req = urllib.request.Request(url, headers=headers)

# 2. 获取响应对象
res = urllib.request.urlopen(req)

# 3. 读取响应对象
html = res.read().decode("utf-8")

# 4. 具体操作
# print(html)
print(res.getcode())
print(res.geturl())

```

    200
    https://www.baidu.com/


- urllib.parse模块
    - urlencode(字典)  ## 给中文编码，三个百分号一个汉子，注意：参数一定要为字典。
    - 实例见urlrequest.py


```python
import urllib.parse
meinv = {"wd":"美女"}
meinv = urllib.parse.urlencode(meinv)
print(meinv)
```

    wd=%E7%BE%8E%E5%A5%B3



```python
import urllib.request
import urllib.parse


# 拼接URL
baseurl = "http://www.baidu.com/s?"
key = input("请输入要搜索的内容：")
# 进行urlencode()编码
key = urllib.parse.urlencode({"wd":key})
url = baseurl + key

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}

# 创建请求对象
req = urllib.request.Request(url, headers=headers)

# 获取响应对象
res = urllib.request.urlopen(req)
html = res.read().decode("utf-8")

# 写入文件
with open("搜索.html", "w", encoding='utf-8') as f:
    f.write(html)
```

- quote(字符串编码)
- unquote(字符串解码)


```python
  key = urllib.parse.quote("字符串")
  baseurl = "http://www.baidu.com/s?wd="
  key = input("请输入要搜索的内容:")
  #进行quote()编码
  key = urllib.parse.quote(key)
  url = baseurl + key
  print(url)
```

### 练习
- 百度贴吧数据抓取
- 要求：
    1. 输入要抓取的贴吧名称
    2. 输入爬取的起始页和终止页
    3. 把每一页的内容保存到本地
        - 第1页.html 第2页.html ... ... 
- 步骤：
  1. 找URL规律,拼接URL
     - 第1页：http://tieba.baidu.com/f?kw=美女&pn=0
     - 第2页：http://tieba.baidu.com/f?kw=美女&pn=50
     - 第3页：http://tieba.baidu.com/f?kw=美女&pn=100
     - 第n页：pn=(n-1)*50
  2. 获取网页内容(发请求获响应)
  3. 保存(本地文件、数据库)

### 请求方式及实例
- GET
    1. 特点 ：查询参数在URL地址中显示
    2. 案例 ：抓取百度贴吧
    
    
- POST(在Request方法中添加data参数)
    1. urllib.request.Request(url,data=data,headers=headers)
        - data：表单数据以bytes类型提交,不能是str
    2. 处理表单数据为bytes类型
        1. 把Form表单数据定义为字典data
        2. urlencode(data)
        3. 转为bytes数据类型：bytes()
    3. 有道翻译案例
    4. 有道翻译返回的是json格式的字符串,如何把json格式的字符串转换为Python中字典
            import json
            r_dict = json.loads(r_json)


```python
import urllib.request
import urllib.parse
import json


# 请输入你要翻译的内容
key = input("请输入要翻译的内容：")
# 把提交的form表单数据转换为bytes数据类型
data = {'i':key,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':'15567713651723',
        'sign':'3eee1e0b9cbebd65a65007f497a9b33a',
        'ts':'1556771365172',
        'bv':'d1dc01b5ffc1e7dfd53e6ee3c347fc81',
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTlME'
        }
# 字符串i=key&from=AUTO&to=AUTO&s....
data = urllib.parse.urlencode(data)
data = bytes(data, "utf-8")
# 发请求，获取相应
# url为POST地址，抓包工具抓到的
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
# 此处data为form表单数据，为bytes数据类型
req = urllib.request.Request(url, data=data, headers=headers)
res = urllib.request.urlopen(req)
r_json = res.read().decode("utf-8")

r_dict = json.loads(r_json)
print(r_dict["translateResult"][0][0]["tgt"])
```

    请输入要翻译的内容：天堂
    heaven

