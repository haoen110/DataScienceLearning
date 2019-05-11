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
    print(driver.page_source.find("美女"))


test2()

