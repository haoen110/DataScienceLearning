from selenium import webdriver
import time
import csv


# 接收用户输入，访问京东
pro = input("请输入要爬取的商品：")
driver = webdriver.Chrome()
driver.get("https://www.jd.com/")
# 发送文字到搜索框
ss = driver.find_element_by_class_name("text")
ss.send_keys(pro)
bt = driver.find_element_by_class_name("button")
bt.click()
time.sleep(1)

while True:
    # 动态加载 -> 全部加载
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)') # 执行JS脚本，拉到底部
    time.sleep(2)
# 正常解析爬取
    r_list = driver.find_elements_by_xpath('//div[@id="J_goodsList"]//li')
    for r in r_list:
        m = r.text.split('\n')
        price = m[0]
        name = m[1]
        com = m[2]
        store = m[3]
        with open("info.csv", 'a', newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            L = [name, price, store, com]
            writer.writerow(L)
    break

# 点击下一页
# .......





driver.close()