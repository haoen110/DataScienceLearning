from selenium import webdriver
import csv


def pld(y, m, d):
    if m in big_month:
        d += 1
        if d == 32:
            d = 1
            m += 1
    elif m != 2:
        d += 1
        if d == 31:
            d = 1
            m += 1
    else:
        rn = [1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
        if y not in rn:
            d += 1
            if d == 29:
                d = 1
                m += 1
        else:
            d += 1
            if d == 30:
                d = 1
                m += 1

    if m == 13:
        m = 1
        y += 1
        d = 1
    return y, m, d


def spider(driver, base_url, year, month, date):
    url = base_url + str(year) + '-' + str(month) + '-' + str(date)
    driver.get(url)
    driver.implicitly_wait(50)
    r_list = driver.find_elements_by_xpath('//div[@class="observation-table"]//tbody/tr')
    for r in r_list:
        day = str(year) + '-' + str(month) + '-' + str(date)
        # Time
        tm = r.find_element_by_xpath('./td[1]').text
        # Temperature
        temperature = r.find_element_by_xpath('./td[2]').text
        # dew point
        dew_point = r.find_element_by_xpath('./td[3]').text
        # humidity
        humidity = r.find_element_by_xpath('./td[4]').text
        # wind
        wind = r.find_element_by_xpath('./td[5]').text
        # wind speed
        wind_speed = r.find_element_by_xpath('./td[6]').text
        # pressure
        pressure = r.find_element_by_xpath('./td[8]').text

        print([day, tm, temperature, dew_point, humidity, wind, wind_speed, pressure])

        with open("./info.csv", 'a', newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            L = [day, tm, temperature, dew_point, humidity, wind, wind_speed, pressure]
            writer.writerow(L)


option = webdriver.ChromeOptions()
option.add_argument("headless")
driver = webdriver.Chrome(chrome_options=option)
base_url = 'https://www.wunderground.com/history/daily/cn/shenzhen/ZGSZ/date/'
big_month = [1, 3, 5, 7, 8, 10, 12]
start_year = int(input("请输入开始年份："))
start_month = int(input("请输入月份："))
start_date = int(input("请输入日期："))
end_year = int(input("请输入结束年份："))
end_month = int(input("请输入月份："))
end_date = int(input("请输入日期："))
start = [start_year, start_month, start_date]
end = [end_year, end_month, end_date]
year = start[0]
month = start[1]
date = start[2]

flag = 1
while flag == 1:
    print('正在爬取：', year, month, date)
    spider(driver, base_url, year, month, date)
    year, month, date = pld(year, month, date)
    if [year, month, date] == end:
        flag = 0

driver.close()