from selenium import webdriver
import time
import csv
import requests

driver = webdriver.Chrome()
driver.get("https://mall.jd.com/view_search-997283-8874844-99-1-24-1.html")
# 一级：//ul[@class='gl-warp clearfix']
# 二级：./li
# 名称：.//div[@class='jDesc']/a
# 现价：.//span[@class='jdNum']
# 评价：.//em[@class='jCommentNum']
# 宝贝链接：.//div[@class='jDesc']/a/@href

def write_image(img_link, name):
    res = requests.get(img_link, headers={"User-Agent": "Mozilla/5.0"})
    res.encoding = 'utf-8'
    html = res.content
    filename = name
    with open('./pics/'+filename+'.jpg', 'wb') as f:
        f.write(html)
        print("%s下载成功" % filename)

i = 1
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')  # 执行JS脚本，拉到底部
    time.sleep(1)
    r_list = driver.find_elements_by_xpath('//ul[@class="gl-warp clearfix"]/li')
    for r in r_list:
        name = r.find_element_by_xpath('.//div[@class="jDesc"]/a').text
        pic = r.find_element_by_xpath('.//div[@class="jPic"]//img').get_attribute("src")
        time.sleep(1)
        write_image(pic, name)

    print("第%d页爬取成功..." % i)
    # 点击下一页
    # if driver.page_source.find("jPageDisable") == -1:
    if i != 21:
        driver.find_element_by_xpath('//div[@class="jPage"]/a[text()="下一页 >"]').click()
        time.sleep(1)
        i += 1
    else:
        print("爬取完毕，共%d页！" % i)
        driver.close()
        break

# .......
