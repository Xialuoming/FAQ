import orm
from sqlalchemy import or_

def InserAccount(user, password, title, salary):
	with orm.session_scope() as session:
		account = orm.Account(user_name=user, password=password, title=title, salary=salary)
		session.add(account)

def GetAccount(id=None, user_name=None):
	with orm.session_scope() as session:
		return session.query(orm.Account).filter(
			or_(orm.Account.id == id, orm.Account.user_name == user_name)).first()

def DeleteAccount(user_name):
	with orm.session_scope() as session:
		account = GetAccount(user_name=user_name)
		if account:
			session.delete(account)

def UpdateAccount(id, user_name, password, title, salary):
	with orm.session_scope() as session:
		account = session.query(orm.Account).filter(orm.Account.id == id).first()
		if not account: return 
		account.user_name=user_name
		account.password=password
		account.salary=salary
		account.title=title

# import MySQLdb
# conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root123',db='yuanjian',port=3306)
# cur = conn.cursor()

# cur.execute("CREATE TABLE yj(id int auto_increment not null primary key,user_name char(8) not null,password char(40) not null,title char(100),salary char(10));")

InserAccount('yuanjian', '123', 'system manager', '7k')
InserAccount('yangying', '321', 'baby', 'k7')
print GetAccount(2)

DeleteAccount('yuanjian')
UpdateAccount(1, 'admin', 'none', 'system manager', '8k')