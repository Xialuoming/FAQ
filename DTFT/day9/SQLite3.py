# import sqlite3

# conn = sqlite3.connect('test.db')
import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root123',db='yuanjian',port=3306)
cur = conn.cursor()

cur.execute("CREATE TABLE demo(num int,str varchar(20));")
cur.execute("INSERT INTO demo VALUES(%d, '%s')" % (1, 'aaa'))
cur.execute("INSERT INTO demo VALUES(%d, '%s')" % (2, 'bbb'))
cur.execute("INSERT INTO demo VALUES(%d, '%s')" % (3, 'ccc'))
cur.execute("UPDATE demo SET str='%s' WHERE num = %d" % ('ddd', 3))
cur.execute("SELECT distinct * FROM demo;")
rows = cur.fetchall()
print 'number of records: ', len(rows)
for i in rows:
	print i
cur.execute("Drop TABLE demo;")

conn.commit()

cur.close()

conn.close()