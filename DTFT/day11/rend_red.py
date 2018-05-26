from flask import Flask
from flask import render_template
from flask import Markup
from flask import abort, redirect

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
	a = Markup('<strong>Hi %s</strong>') % '<blink>David</blink>'
	return render_template('hello.html', name=name, a=a)

@app.route('/')
def index():
	return redirect('/check')
	# return redirect(url_for(f_check))
@app.errorhandler(400)
def bad_request(error):
	return render_template('bad_request.html'), 400

@app.route('/check')
def f_check():
	abort(400)

@app.route('/Message/', methods=['POST'])
def do_send():
	return 'POST'

@app.route('/Message/', methods=['GET'])
def show_the_send_from():
	return 'GET'
if __name__ == '__main__':
	app.run(host='127.0.0.2',port=80, debug=False)


