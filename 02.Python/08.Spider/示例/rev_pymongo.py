import pymongo

# 创建连接对象
conn = pymongo.MongoClient("localhost", 27017)

# 创建数据库对象，spiderdb为库的名字
db = conn.spiderdb

# 利用数据库对象创建集合对象
myset = db.t1

# 执行插入
myset.insert({"name":"Tom"})
# show dbs
# use spiderdb
# show tables
# db.t1.find().pretty()

