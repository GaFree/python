import pymysql

"""导入连接MySQL需要的包，没有安装pymysql需要先安装
使用命令行切换到python的安装路径下的scripts子目录下安装（pip install pymysql）
"""
# 连接MySQL数据库
db = pymysql.connect("localhost", "root", "123456", "python_conn", charset='utf8')
"""五个参数分别为 主机名，用户名，密码，所要连接的数据库名，为了解决中文乱码问题的字符集"""
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用execute()方法执行sql语句
sql = 'select * from test_conn'

cursor.execute(sql)
# 使用fetchone()方法获取所有数据
results = cursor.fetchall()
# 打印
for row in results:
    sid = row[0]
    name = row[1]
    age = row[2]
    sclass = row[3]
    print(sid, name, age, sclass)
# 关闭数据库
db.close()
