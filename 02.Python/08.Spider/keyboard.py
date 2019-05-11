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
