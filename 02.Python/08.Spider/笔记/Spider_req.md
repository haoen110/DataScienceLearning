
# requests模块
1. 安装(用管理员身份去打开Anaconda Prompt)
    - `conda install requests`
    - `python -m pip install requests` # 以管理员身份去执行pip安装命令
2. 常用方法
    1. get(url,headers=headers)：发起请求,获取响应对象
    2. response属性
        - `response.text`：返回字符串类型
        - `response.content`：返回bytes类型，应用场景：爬取非结构化数据
        - `response.encoding`：一般返回 ：ISO-8859-1
        - `response.encoding` = "utf-8"：制定编码格式
        - `response.status_code`：返回服务器响应码
        - `response.url`：返回数据的URL地址
    3. get()使用场景
        - 没有查询参数：res = requests.get(url,headers=headers)
        - 有查询参数：params={}，注：params参数必须为字典,自动进行编码
    4. post() 参数名：data
        - data = {}


```python
import requests


url = "http://www.baidu.com/"
headers = {"Uesr-Agent":"Mozilla/5.0"}
# 发请求获相应
response = requests.get(url, headers=headers)

# 获取响应对象内容
# print(response.text)
# 获取编码类型
print(response.encoding)
# 更改编码
response.encoding = "utf-8"
print(response.text)

# 获取字节流
print(response.content)

# 获取响应码
print(response.status_code)

# 返回url
print(response.url)

# get参数
url = "http://www.baidu.com/s?"
key = input("请输入搜索的内容：")
params = {"wd": key}

res = requests.get(url, params=params, headers=headers)
# 指定utf-8
res.encoding = "utf-8"
print(res.text)
```

### 代理(参数名：proxies)
1. 获取代理IP的网站
    - 西刺代理网站
    - 快代理
    - 全网代理
    - 查看自己的ip：`https://www.whatismyip.com/`
2. 普通代理
    - `proxies = {"协议":"协议://IP地址:端口号"}`
        - 183.129.207.82	11597
        - 183.230.177.118	8060
3. 私密代理
    - `proxies = {"http":"http://309435365:szayclhp@123.206.119.108:21081"}`

## 案例1: 安居客


```python
import requests
import re
import csv
import time
import pymongo

# 读取文件尝试
# p = re.compile('<span class="comm-address" title="(.*?)&nbsp;&nbsp;(.*?)">.*?<span class="price-det"><strong>(.*?)</strong>.*?"unit-price">(.*?)</span>', re.S)
# with open('./html.txt') as f:
#     txt = f.read()
# html = p.findall(txt)


headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
url = "https://nb.anjuke.com/sale/gaoxinquz/"

def load_page(url):
    # proxies = {"https":"https://110.178.48.14:56754"}
    res = requests.get(url, headers=headers)
    p = re.compile('<div class="details.*?<span>(.*?)</span><em class.*?<span>(.*?)m²</span>.*?<span class="comm-address" title="(.*?)&nbsp;&nbsp;(.*?)">.*?<span class="price-det"><strong>(.*?)</strong>.*?"unit-price">(.*?)元/m²</span>', re.S)
    html = p.findall(res.text)
    return html

def write_page(r_list):
    for r_tuple in r_list:
        with open("ajk.csv", "a", newline='') as f:  # 开头不空行
            # 创建写入对象
            writer = csv.writer(f)
            L = [i for i in r_tuple]
            writer.writerow(L)


def write_mongo(html):
    conn = pymongo.MongoClient("localhost", 27017)
    db = conn.spiderdb
    myset = db.anjuke
    for r_tuple in html:
        D = {"房型":r_tuple[0],
             "大小":r_tuple[1],
             "小区":r_tuple[2],
             "位置":r_tuple[3],
             "总价":r_tuple[4],
             "单价":r_tuple[5]}
        myset.insert(D)


for i in range(10):
    url = url + "p" + str(i+1) + "/"
    html = load_page(url)
    write_mongo(html)
    # write_page(html)
    time.sleep(1)
```

### Web客户端验证(参数名:auth)
- `auth=("用户名","密码")`
   - `auth=("tarenacode","code_2013")`
   
### SSL证书认证(参数名:verify)
   - verify = True : 默认,进行SSL证书认证
   - verify = False: 不做认证
       - 例如有些http没有认证，需要修改


```python
import requests

url = "https://www.12306.cn/mormhweb/"
headers = {"User-Agent":"Mozilla/5.0"}

res = requests.get(url, headers=headers, verify=False) #
res.encoding = "utf-8"
print(res.text)
```

>## urllib.request中Handler处理器
1. 定义
    - 自定义的urlopen()方法,urlopen()方法是一个特殊的opener(模块已定义好),不支持代理等功能,通过Handler处理器对象来自定义opener对象
2. 常用方法
    - build_opener(Handler处理器对象) ：创建opener对象
    - opener.open(url,参数)
3. 使用流程
    1. 创建相关的Handler处理器对象
        - http_handler = urllib.request.HTTPHandler()
    2. 创建自定义opener对象
        - opener = urllib.request.build_opener(http_handler)
    3. 利用opener对象打开url
        - req = urllib.request.Request(url,headers=headers)
        - res = opener.open(req)
4. Handler处理器分类
    - HTTPHandler()：没有任何特殊功能
    - ProxyHandler(普通代理)
        - 代理: {"协议":"IP地址:端口号"}
    - ProxyBasicAuthHandler(密码管理器对象)：私密代理
    - HTTPBasicAuthHandler(密码管理器对象)：web客户端认证
    - 密码管理器对象作用
        - 私密代理
        - Web客户端认证
        - 程序实现流程
            1. 创建密码管理器对象
                - `pwdmg = urllib.request.HTTPPasswordMgrWithDefaultRealm()`
            2. 把认证信息添加到密码管理器对象
                - `pwdmg.add_password(None,webserver,user,passwd)`
            3. 创建Handler处理器对象
                - 私密代理
                    - `proxy = urllib.request.ProxyAuthBasicHandler(pwdmg)`
                - Web客户端
                    - `webbasic = urllib.request.HTTPBasicAuthHandler(pwdmg)`


```python
'''Handler处理器示例.py'''
import urllib.request

url = "http://www.baidu.com/"
# 创建Handler处理器对象
http_handler = urllib.request.HTTPHandler()
#proxy_handler = urllib.request.ProxyHandler()
# 创建自定义的opener对象
opener = urllib.request.build_opener(http_handler)
# 利用opener对象的open()方法发请求
req = urllib.request.Request(url)
res = opener.open(req)
print(res.read().decode("utf-8"))
```


```python
'''12_ProxyHandler示例.py'''
import urllib.request

url = "http://www.baidu.com/"
proxy = {"http":"127.0.0.1:8888"}
# 创建Handler处理器对象
pro_hand = urllib.request.ProxyHandler(proxy)
# 创建自定义opener对象
opener = urllib.request.build_opener(pro_hand)
# opener对象open方法发请求
req = urllib.request.Request(url)
res = opener.open(req)
print(res.read().decode("utf-8"))
```
