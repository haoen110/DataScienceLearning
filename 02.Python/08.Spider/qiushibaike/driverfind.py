from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.qiushibaike.com/")

# 查找单个节点
r_one = driver.find_element_by_class_name("recmd-content")
print(r_one.text)

# 查找多个节点
r_many = driver.find_elements_by_class_name("recmd-content")
print(r_many)

for r in r_many:
    print(r.text)


driver.quit()