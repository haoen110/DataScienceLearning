import requests


url = "http://www.baidu.com/"
headers = {"Uesr-Agent":"Mozilla/5.0"}
# 发请求获相应
response = requests.get(url, headers=headers)

# 获取响应对象内容
# print(response.text)
# 获取编码类型
print(response.encoding)
# 更改编码
response.encoding = "utf-8"
print(response.text)

# 获取字节流
print(response.content)

# 获取响应码
print(response.status_code)

# 返回url
print(response.url)

# get参数
url = "http://www.baidu.com/s?"
key = input("请输入搜索的内容：")
params = {"wd": key}

res = requests.get(url, params=params, headers=headers)
# 指定utf-8
res.encoding = "utf-8"
print(res.text)




