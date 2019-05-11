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