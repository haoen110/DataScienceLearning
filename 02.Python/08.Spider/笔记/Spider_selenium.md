
# json模块
- 什么是json?
    - javascript中的对象和数组
    - 对象：`{key:value}`取值：对象名.key
    - 数组：`[...,...]`取值：数组[索引值]
- 作用
    - json格式的字符串和Python数据类型之间的转换
- 常用方法
    1. json.loads():json格式 --> Python数据类型
              json      python
              对象      字典
              数组      列表
    2. json.dumps() : Python数据类型 --> json格式
              python       json
              字典         对象
              列表         数组
              元组         数组
        - json.dumps()默认使用ascii编码
        
        
	2. 添加参数ensure_ascii=False,禁用ascii编码

- 动态网站数据抓取 - Ajax
    - 特点 ：滚动鼠标滑轮时加载
    - 抓包：查询参数在 WebForms -> QueryString
    - 案例 ：豆瓣电影排行榜数据抓取
        - 抓取目标：
            - 豆瓣电影 - 排行榜 - 剧情 
            - 电影名称 、评分
        - 代码实现


```python
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
```

# selenium + phantomjs 强大的网络爬虫组合
### selenium
- 定义：Web自动化测试工具,应用于Web自动化测试
- 特点：
    - 可以运行在浏览器,根据指定命令操作浏览器,让浏览器自动加载页面
    - 只是工具,不支持浏览器功能,需要与第三方浏览器结合使用
    
### phantomjs
- 定义：无界面浏览器(无头浏览器)
- 特点：
    - 把网站加载到内存进行页面加载
    - 运行高效
- 安装：
    - Windows
        - 将下载的可执行文件放到Python安装目录的Scripts目录下
	    - `C:\Python36\Scripts`
    - Ubuntu
        - 将下载的phantomjs放到一个路径下
	- 添加环境变量：
        - `vi .bashrc 添加`
        - `export PHANTOM_JS=/home/.../phantomjs-2.1.1-...`
        - `export PATH=$PHANTOM_JS/bin:$PATH`
	    - 终端：source .bashrc
	    - 终端：phantomjs

### Chrome
1. 到[ChromeDriver - WebDriver for Chrome](http://chromedriver.chromium.org/)下载适配自己Chrome浏览器的版本。
2. 将解压出的chromedriver添加到环境变量，或者放到miniconda/bin下（本人使用conda作文环境管理器）


```python
from selenium import webdriver
import time

# 创建浏览器对象
# driver = webdriver.PhantomJS(executable_path='xxxxx')
# driver = webdriver.PhantomJS(executable_path="/Users/haoen110/phantomjs-2.1.1-macosx/bin/phantomjs")
# driver = webdriver.Chrome(executable_path='/Users/haoen110/chromedriver')


def test1():
    # 创建浏览器对象
    driver = webdriver.Chrome()
    # 发请求get()
    driver.get("http://www.baidu.com/")
    # 获取网页截屏
    driver.save_screenshot("百度.png")
    # print("图片保存成功！")
    # 关闭
    driver.quit()


def test2():
    # 创建浏览器对象
    driver = webdriver.Chrome()
    # 打开页面
    driver.get("http://www.baidu.com/")
    # 发送文字到搜索框
    kw = driver.find_element_by_id("kw")
    kw.send_keys("美女")
    # 点击"百度一下"
    su = driver.find_element_by_id("su")
    su.click()
    time.sleep(1)
    # 获取截屏
    # driver.save_screenshot("百度.png")
    # 关闭浏览器
    # driver.quit()
```

### 常用方法
- `driver.get(url)`
- `driver.page_source`：获取响应的html源码
- `driver.page_source.find("字符串")`
    - 作用：从html源码中搜索指定字符串
        - -1：查找失败
        - 非-1：查找成功
- 单元素查找
    - `driver.find_element_by_id("").text`
    - `driver.find_element_by_class_name("")`
    - `driver.find_element_by_xpath('xpath表达式')`
    - 如果匹配到多个节点,则只返回第1个节点对象
- 多元素查找
    - `driver.find_elements_by_....`
        - 如果结果1个,则返回节点对象,不是列表
        - 如果结果N个,则返回列表
- `对象名.send_keys("内容")`
- `对象名.click()`

### 案例1 ：登录豆瓣网站


```python
from selenium import webdriver
import time


# 创建浏览器对象，发送请求
driver = webdriver.Chrome()
driver.get("https://www.douban.com/")
time.sleep(1)
# 获取截图(验证码）
# driver.save_screenshot("验证码.png")
# 找用户名、密码、验证、登录豆瓣按钮
mmdl = driver.find_element_by_class_name("account-tab-account")
mmdl.click()

uname = driver.find_element_by_name("username")
uname.send_keys("haoen110@163.com")

pwd = driver.find_element_by_name("password")
pwd.send_keys("Howie1996925")

button = driver.find_element_by_class_name("btn btn-account")
# 关闭浏览器
```

### 操作键盘
- 导模块
    - from selenium.webdrier.common.keys import Keys


```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 创建浏览器对象，发请求
driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
# 在百度搜索输入Python
kw = driver.find_element_by_id("kw")
kw.send_keys("Python")
time.sleep(0.8)
# 全选：ctrl + a
kw = driver.find_element_by_id("kw")
kw.send_keys(Keys.COMMAND, 'a')
time.sleep(0.8)
# 剪切：ctrl + x
kw = driver.find_element_by_id("kw")
kw.send_keys(Keys.COMMAND, 'x')
time.sleep(0.8)
# 粘贴：ctrl + v
kw = driver.find_element_by_id("kw")
kw.send_keys(Keys.COMMAND, 'v')
time.sleep(0.8)
# 清空搜索框
kw = driver.find_element_by_id("kw")
kw.clear()
time.sleep(0.8)
# 输入
kw = driver.find_element_by_id("kw")
kw.send_keys("Spider")
# 搜索
su = driver.find_element_by_id("su")
su.click()
```

### Chromdriver如何设置无界面模式
- opt = webdriver.ChromeOptions()
- opt.set_headless()
- driver = webdriver.Chrome(options=opt)
- driver.get(url)

### 案例2 ：斗鱼直播网站主播信息抓取（JS分页加载）
- 抓取目标：主播名称、观众人数
    1. 主播：class -> dy-name ellipsis fl
        - `//div[@id="live-list-content"]//span[@class="dy-name ellipsis fl"]`
    2. 人数：class -> dy-num fr
        - `//div[@id="live-list-content"]//span[@class="dy-num fr"]`
    3. 下一页按钮(能点)：
        - `class -> shark-pager-next`
    4. 下一页按钮(不能点)
        - `class -> shark-pager-next shark-pager-disable shark-pager-disable-next`


```python
'''11_斗鱼直播抓取案例.py'''
from selenium import webdriver
from lxml import etree
import time

# 把Chrome设置无界面浏览器
opt = webdriver.ChromeOptions()
opt.set_headless()
# 创建浏览器对象,发请求
driver = webdriver.Chrome(options=opt)
driver.get("https://www.douyu.com/directory/all")
i = 1

# 循环
while True:
    # 解析(driver.page_source)
    # 获取主播名称 和 观众人数
    parseHtml = etree.HTML(driver.page_source)
    names = parseHtml.xpath('//div[@id="live-list-content"]//span[@class="dy-name ellipsis fl"]')
    numbers = parseHtml.xpath('//div[@id="live-list-content"]//span[@class="dy-num fr"]')
    
    for name,number in zip(names,numbers):
        print("\t主播名称：%s \t观众人数：%s" %
              (name.text.strip(),number.text.strip()))
        #for name,number in [("主播1","20万"),("主播2","15万")]
    print("第%d页爬取成功" % i)
    i += 1
    # 判断是否需要点击下一页
    # 能点 ：点击,继续循环
    if driver.page_source.find("shark-pager-disable-next") == -1:
        driver.find_element_by_class_name("shark-pager-next").click()
        time.sleep(1)
    else:
        break
    # 不能点 ：break

print("一共爬取了%d页" % i)
```

### 案例3：京东商品爬取
- 目标
    - 商品名称
    - 商品价格
    - 评论数量
    - 商家名称


```python

```
