import json


# json格式的数组
jsarray = '[1,2,3,4]'
# 数组 -> 列表
L = json.loads(jsarray)
print(L)
print(type(L))

# json 格式对象
jsobj = '{"city": "天地会", "name": "步惊云"}'
# 对象 -> 字典
D = json.loads(jsobj)
print(D)
print(type(D))

# python -> json
L = [1, 2, 3, 4]
T = (1, 2, 3, 4)
D = {'city': '天地会', 'name': '步惊云'}
jsarray1 = json.dumps(L)
jsarray2 = json.dumps(T)
jsobj1 = json.dumps(D)
print(jsarray1, type(jsarray1))
print(jsarray2, type(jsarray2))
print(jsobj1, type(jsobj1))