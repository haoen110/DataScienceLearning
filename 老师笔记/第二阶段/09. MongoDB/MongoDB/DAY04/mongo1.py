from pymongo import MongoClient 

conn = MongoClient('localhost',27017)

db = conn.stu 

myset = db.class0 

#索引操作
#默认创建正向索引
# index = myset.ensure_index('name')
# print(index)

#创建逆向索引
# index = myset.ensure_index([('age',-1)])

#获取当前集合中索引
# for i in myset.list_indexes():
#     print(i)

#删除所有索引
# myset.drop_indexes()

#删除单个索引
# myset.drop_index("name_1")

#其他索引类型

#复合索引
# myset.ensure_index([('name',1),('age',-1)])

#唯一索引
# myset.ensure_index('name',\
#     name = "MyIndex",unique = True)

#稀疏索引
# myset.ensure_index('age',sparse = True)

#聚合操作
myset1 = db.class4 

p = [
     {'$group':{'_id':'$King','count':{'$sum':1}}},
     {'$match':{'count':{'$gt':1}}},
    ]

cursor = myset1.aggregate(p)

for i in cursor:
    print(i)

conn.close()