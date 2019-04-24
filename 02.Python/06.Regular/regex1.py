import re 

it = re.finditer(r'\d+',"2008-2018 10年，\
    中国发生了翻天覆地的变化")

for i in it:
    print(i.group())


#fullmatch
try:
    obj = re.fullmatch(r"\w+",'abcdef123')
    print(obj.group())
except AttributeError as e:
    print(e)

#match
obj = re.match(r'foo',"foo,food on the table")
print(obj.group())

#search
obj = re.search(r'foo',"Foo,food on the table")
print(obj.group())