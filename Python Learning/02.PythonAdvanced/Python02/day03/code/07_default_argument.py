

# 以下示意函数的缺省参数
def info(name, age=1, address="未填写"):
    print(name, "今年",
          age, '岁, 家庭地址是:', address)


info('tarena', 15)
info('小魏', 20, '北京市朝阳区')
info('小李')
