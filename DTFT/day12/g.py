from flask import g
from flask import Flask,session
app = Flask(__name__)

class MyDB():
	def __init__(self):
		print 'A db connection is created'

	def close(self):
		print 'A db is closed'

def connect_to_database():
	return MyDB()

def get_db():
	db = getattr(g, '_database', None)
	print db,'222222222222'
	if db is None:
		db = connect_to_database()
		g._database = db
	print db,'3333333333'
	return db

#teardown_db 在请求结束后自动被flask框架调用
@app.teardown_request
def teardown_db(response):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()

def login():
	db = get_db()
	session["has_login"] = True

@app.route('/view_list')
def view_list():
	print session
	if "has_login" not in session:
		login()
		print '"has_login" not in session'
	db = get_db()
	return 'teardown_db() will be called automatically'

if __name__ == '__main__':
	app.secret_key = '346' #建立回话秘钥
	app.run()