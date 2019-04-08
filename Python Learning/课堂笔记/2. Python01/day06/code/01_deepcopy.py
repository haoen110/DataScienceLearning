# 01_deepcopy.py

# 此程序示意 深拷贝

import copy  # 导入copy模块
L = [3.1, 3.2]
L1 = [1, 2, L]
L2 = copy.deepcopy(L1) # 深拷贝
print(L1)  # [1, 2, [3.1, 3.2]]
print(L2)  # [1, 2, [3.1, 3.2]]
L2[2][0] = 3.14
print(L1)  # [1, 2, [3.1, 3.2]]
print(L2)  # [1, 2, [3.14, 3.2]]

