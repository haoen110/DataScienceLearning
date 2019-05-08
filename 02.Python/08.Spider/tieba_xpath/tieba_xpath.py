'''百度贴吧图片抓取'''
import requests
from lxml import etree


class TiebaImageSpider:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.baseurl = 'https://tieba.baidu.com'
        self.pageurl = 'https://tieba.baidu.com/f?'

    # 获取所有帖子URL列表
    def get_page_url(self, params):
        res = requests.get(self.pageurl, params=params, headers=self.headers)
        res.encoding = 'utf-8'
        print(res.url)
        html = res.text
        parse_html = etree.HTML(html)
        t_list = parse_html.xpath('//div[contains(@class,"t_con")]/div/div/div/a/@href')
        print(t_list)
        for t_link in t_list:
            t_link = self.baseurl + t_link
            self.get_image_url(t_link)

    # 获取帖子中图片URL列表
    def get_image_url(self, t_link):
        res = requests.get(t_link, headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        parse_html = etree.HTML(html)
        img_list = parse_html.xpath('//img[@class="BDE_Image"]/@src')
        for img_link in img_list:
            self.write_image(img_link)

    # 保存到本地
    def write_image(self, img_link):
        res = requests.get(img_link, headers=self.headers)
        res.encoding = 'utf-8'
        html = res.content
        filename = img_link[-12:]
        with open(filename, 'wb') as f:
            f.write(html)
            print("%s下载成功" % filename)

    # 主函数
    def main(self):
        name = input("请输入贴吧名字：")
        begin = int(input("请输入起始页："))
        end = int(input("请输入中止页："))
        for n in range(begin, end + 1):
            pn = (n - 1) * 50
            params = {'kw': name,
                      'pn': str(pn)}
            self.get_page_url(params)

# s = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
# s = '//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a/@href'
# s2 = '//cc/div/img[@class="BDE_Image"]/@src'


if __name__ == '__main__':
    spider = TiebaImageSpider()
    spider.main()