# -*- coding: utf-8 -*-
# 导入mysql驱动
import mysql.connector

# 创建数据库连接对象，如果数据库未创建，需要首先通过mysql命令行创建。创建数据库命令 create database <db_name>
conn = mysql.connector.connect(user='root', password='password', database='test')

# 通过数据库连接对象获得游标对象
cur = conn.cursor()
# cur.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 参数值的引号需要转义
# cur.execute('insert into user (id, name) values (\'1\', \'aaa\')')
# 参数可以是tuple，也可以是list。mysql的sql语句占位符是%s
# cur.execute('insert into user (id, name) values (%s, %s)', ('2', 'bbb'))
# cur.execute('insert into user (id, name) values (%s, %s)', ['3', 'ccc'])
print(cur.rowcount)
conn.commit()
cur.execute('select * from user where id = %s', ('1',))
values = cur.fetchall()
for i in values:
    print(i)
cur.execute('select * from user where name = %s', ['bbb'])
values = cur.fetchall()
print(values)
# 关闭游标和连接对象
cur.close()
conn.close()