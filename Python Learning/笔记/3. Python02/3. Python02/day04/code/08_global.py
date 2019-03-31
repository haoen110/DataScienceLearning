# 08_global.py

# 此示例示意global语句的用法
v = 100

def fn():
    global v
    v = 200

fn()
print(v)  # 200
