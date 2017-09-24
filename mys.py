import MySQLdb

db = MySQLdb.connect('127.0.0.1', 'sami', '1111', 'sami')
cur = db.cursor()
sql = 'select * from userlist'
cur.execute(sql)
rs = cur.fetchall()
print(rs)
cur.close()
db.close()