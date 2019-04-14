

# 此程序用于示意导入'小张'写的模块mymod1
# 并调用相应的数据和函数

import mymod1  # 导入模块 mymod1.py
mymod1.myfun1()  # 调用mymod1里的myfun1() 函数
print(mymod1.name1)  # audi


from mymod1 import name2
print("mymod1里的name2为: ", name2)


from mymod1 import *
myfun2()


