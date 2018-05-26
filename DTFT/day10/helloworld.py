from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_flask():
	return 'Hello, World'

@app.route('/school')
def schools():
	return 'school'

@app.route('/student/')
def students():
	return 'student'
	
if __name__ == '__main__':
	app.run(host='127.0.0.2',port=80, debug=False)