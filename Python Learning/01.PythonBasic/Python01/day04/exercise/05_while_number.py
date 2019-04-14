# 2. 写程序，输入二个整数，第一个用begin绑定，
#    第二个用end变量绑定，打印出 begin~end的
#    所有的整数

begin = int(input("请输入第一个整数: "))
end = int(input("请输入第二个整数: "))

i = begin
while i <= end:
    print(i)
    i += 1

