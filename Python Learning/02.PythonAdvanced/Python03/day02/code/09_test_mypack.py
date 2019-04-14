

# 09_test_mypack.py

# 第一种用法
# import mypack.menu  # 导入menu模块
# mypack.menu.show_menu()

# 第二种方法导入menu 模块
# import mypack.menu as m
# m.show_menu()

# 第三种方法
from mypack.menu import show_menu as menu
menu()
