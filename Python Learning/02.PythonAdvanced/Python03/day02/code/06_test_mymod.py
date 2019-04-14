# 06_test_mymod.py


# 此示例示意各模块内的变量不会冲突 

import mymod1
import mymod2

print('mymod1.name1 =', mymod1.name1)
print('mymod2.name1 =', mymod2.name1)

# 以下方法使用，会引起变量名冲突
from mymod1 import *
from mymod2 import *

print(name1)  # 已经发生冲突