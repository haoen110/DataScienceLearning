import requests
from lxml import etree
from queue import Queue
import threading
import time


class BsSpider:
    def __init__(self):
        self.baseurl = "http://www.budejie.com/"
        self.headers = {"User_Agent": "Mozilla/5.0"}
        self.urlQueue = Queue()  # url队列
        self.resQueue = Queue()  # 响应队列

    # 生成URL队列
    def get_url(self):
        for num in range(1, 51):
            url = self.baseurl + str(num)  # 1是第一页
            self.urlQueue.put(url)

    # 响应队列
    def get_html(self):
        while True:
            url = self.urlQueue.get()
            res = requests.get(url, headers=self.headers)
            res.encoding = 'utf-8'
            html = res.text
            # 放到响应队列
            self.resQueue.put(html)
            # 清除此任务
            self.urlQueue.task_done()

    # 解析页面
    def get_content(self):
        while True:
            # 从响应队列中一次获取html源码
            html = self.resQueue.get()
            parse_html = etree.HTML(html)
            r_list = parse_html.xpath('//div[@class="j-r-list-c-desc"]/a/text()')
            for r in r_list:
                print(r + "\n")
            # 清除任务
            self.resQueue.task_done()

    def main(self):
        # 存放所有的线程
        thread_list = []
        # 获取url队列
        self.get_url()
        # 创建getpage线程
        for i in range(3):
            thread_res = threading.Thread(target=self.get_html)
            thread_list.append(thread_res)
        for i in range(2):
            thread_parse = threading.Thread(target=self.get_content)
            thread_list.append(thread_parse)
        # 所有线程开始干活
        for th in thread_list:
            th.setDaemon(True)
            th.start()
        # 如果队列为空，则执行其他程序
        self.urlQueue.join()
        self.resQueue.join()
        print("运行结束")


if __name__ == '__main__':
    begin = time.time()
    spider = BsSpider()
    spider.main()
    end = time.time()
    print("运行时间：", end - begin)
