from selenium import webdriver
import time
import csv

driver = webdriver.Chrome()
driver.get("https://mall.jd.com/view_search-997283-8874844-99-1-24-1.html")

# 一级：//ul[@class='gl-warp clearfix']
# 二级：./li
# 名称：.//div[@class='jDesc']/a
# 现价：.//span[@class='jdNum']
# 评价：.//em[@class='jCommentNum']
# 宝贝链接：.//div[@class='jDesc']/a/@href

i = 1
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')  # 执行JS脚本，拉到底部
    time.sleep(1)
    r_list = driver.find_elements_by_xpath('//ul[@class="gl-warp clearfix"]/li')
    for r in r_list:
        name = r.find_element_by_xpath('.//div[@class="jDesc"]/a').text
        c_price = r.find_element_by_xpath('.//span[@class="jdNum"]').text
        num = r.find_element_by_xpath('.//em[@class="jCommentNum"]').text
        link = r.find_element_by_xpath('.//div[@class="jDesc"]/a').get_attribute("href")
        name = name.split(' ')
        with open("info3.csv", 'a', newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            L = [name[-1], c_price, num, link]
            writer.writerow(L)

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
