from flask import Flask, session
from datetime import datetime
# import time
app = Flask(__name__)

app.secret_key = 'SET_ME_BEFORE_USE_SESSION'

@app.route('/write_session')
def writeSession():
	session['key_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	print session.new,session.modified,'KKKKKKKKKKKKKKK'
	return session['key_time']

@app.route('/read_session')
def readSession():
	print session.new,session.modified,'MMMMMMMMMMMMMMMM'
	return session.get('key_time')

# @app.route('/w_session')
# def wSession():
# 	session['key_time'] = time.time()
# 	print session.modified
# 	return session['key_time']

if __name__ == '__main__':
	app.run()