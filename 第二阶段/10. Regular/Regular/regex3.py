import re 

s = '''hello world
hello kitty
你好,北京'''

pattern = r'''H\w+  #匹配第一个单词
\s+    #匹配多个空格
[a-z]+ #匹配其他
'''

regex = re.compile(pattern,flags = re.X | re.I)

try:
    s = regex.search(s).group()
except:
    print("没有匹配到内容")
else:
    print(s)