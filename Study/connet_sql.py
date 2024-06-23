import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="qgs0051",
    auth_plugin='mysql_native_password',
    # 后面这句，这个错误出现的原因是在mysql8之前的版本中加密规则为mysql_native_password，
    # 而在mysql8以后的加密规则为caching_sha2_password。
    # 建立连接时尝试访问数据库：sendb_zr
    database="sendb_zr",
    buffered=True
)
print(mydb)

# 创建数据库
mycursor = mydb.cursor()
# mycursor.execute("create database sendb_zr") # 已创建，已存在，要注释

# 使用 "SHOW DATABASES" 语句列出系统中的所有数据库，检查数据库是否存在：
mycursor.execute("show databases")
for x in mycursor:
    print(x)

# 创建表 "customers"：已创建，已存在，要注释
# mycursor.execute("create table customer (name varchar(255), address varchar(255))")

# 返回系统中的数据库表：
mycursor.execute("show tables")
for y in mycursor:
    print(y)

# 在已有的表上创建主键：#增加完主键需要注释掉才能继续用此文档
# mycursor.execute("ALTER TABLE sendb_zr.customer ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# 在表“customer”中插入记录：单行 # 注释掉，重复插入
'''sql = "insert into customer (name, address) value (%s, %s)"'''
'''val = ("Sen","zrping 2")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")'''

# 要在表中插入多行，请使用 executemany() 方法。
# executemany() 方法的第二个参数是元组列表，包含要插入的数据：
'''
sql = "insert into customer (name, address) value (%s, %s)"
val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")'''

'''
# 插入一行，并返回 id：
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)
'''

'''
# select from
# 从表“customer”中获取所有记录，并显示结果：
mycursor.execute("select * from customer")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
# 注释：我们用了 fetchall() 方法，该方法从最后执行的语句中获取所有行。

# 仅选择地址和列
mycursor.execute("select name, address from customer")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# 使用 fetchone() 方法
# 如果您只对一行感兴趣，可以使用 fetchone() 方法。
# fetchone() 方法将返回结果的第一行：
mycursor.execute("select * from customer")

myresult = mycursor.fetchone()

print(myresult)
'''

# where 语句筛选数据
# 选择记录为 "Park Lane 38" 的记录，结果：
sql = "SELECT * FROM customer WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# 您也可以选择以给定字母或短语开头、包含或结束的记录。
# 请使用 ％ 表示通配符：
sql = "SELECT * FROM customer WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# 防止 SQL 注入
# 当用户提供查询值时，您应该转义这些值。
# 此举是为了防止 SQL 注入，这是一种常见的网络黑客技术，可以破坏或滥用您的数据库。
# mysql.connector 模块拥有转义查询值的方法：
# 使用占位符 ％s 方法来转义查询值：
sql = "SELECT * FROM customer WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# order by 升降序
sql = "SELECT * FROM customer ORDER BY name"
# 请使用order by ... DESC 关键字按降序对结果进行排序。
sql = "SELECT * FROM customer ORDER BY name DESC"
# 删除地址为 "Mountain 21" 的任何记录：
sql = "DELETE FROM customer WHERE address = 'Mountain 21'"
# mysql.connector 模块使用占位符 ％s 来转义 delete 语句中的值：
sql = "DELETE FROM customer WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

# 删除 "customers" 表：
# sql = "DROP TABLE customers"
# mycursor.execute(sql)
# 删除表 "customers" （如果存在）：
# sql = "DROP TABLE IF EXISTS customers"
# mycursor.execute(sql)

# 把地址列中的 "Valley 345" 覆盖为 "Canyoun 123"：
sql = "UPDATE customer SET address = 'Canyon 123' WHERE address = 'Valley 345'"
# 请注意：语句 mydb.commit()。需要进行更改，否则不会表不会有任何改变。
#
# 使用占位符 ％s 来转义 delete 语句中的值：
sql = "UPDATE customer SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

# 选取 "customers" 表中的前 五条 记录：
mycursor.execute("SELECT * FROM customers LIMIT 5")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# 使用 "OFFSET" 关键字：从位置 3 开始返回 5 条记录：
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

''' # 假设有两个表 users 和 products 表
# users表
{ id: 1, name: 'John', fav: 154},
{ id: 2, name: 'Peter', fav: 154},
{ id: 3, name: 'Amy', fav: 155},
{ id: 4, name: 'Hannah', fav:},
{ id: 5, name: 'Michael', fav:}
# products表
{ id: 154, name: 'Chocolate Heaven' },
{ id: 155, name: 'Tasty Lemons' },
{ id: 156, name: 'Vanilla Dreams' }
'''

# 使用 users 的 fav 字段和 products 的 id 字段来组合这两个表。
# 组合用户和产品，查看用户最喜欢的产品名称：
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# LEFT JOIN
# 在上例中，Hannah 和 Michael 被排除在结果之外，这是因为 INNER JOIN 只显示匹配的记录。
# 如果希望显示所有用户，即使他们没有喜欢的产品，请使用 LEFT JOIN 语句：
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"
# 选择所有产品以及喜欢它们的用户：
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"
