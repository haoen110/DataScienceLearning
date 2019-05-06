import requests
import re
import csv
import time
import pymysql
import getpass

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


def write_mysql(html):
    db = pymysql.connect("localhost", "root", getpass.getpass())
    cursor = db.cursor()
    c_db = "create database if not exists spiderdb"
    u_db = "use spiderdb"
    c_tab = "create table anjuke(id int primary key auto_increment, housetype varchar(30),"
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
