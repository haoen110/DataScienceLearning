# 练习:
#   1. 写一个程序，输入一些单词和解释，将单词作为键，
#     将解释作为值，将这些数据存入字典中.
#     然后:
#       输入查询的单词，显示出此单词的解释 

dictionary = {}
# 读取数据放入字典
while True:
    k = input("请输入单词(直接回车结束): ")
    if not k:
        break
    v = input("请输入解释: ")
    dictionary[k] = v  # 形成键值对放入字典

# 查询单词 (ctrl + c 退出)
while True:
    k = input("请输入要查询的查询的词: ")
    if k in dictionary:
        print("解释:", dictionary[k])
    else:
        print("单词不存在")






