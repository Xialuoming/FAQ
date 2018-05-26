from flask import request, url_for, redirect
from flask import Flask

app = Flask(__name__)

@app.route('/redirect_url')
def redirect_url():
	next = request.args.get('next') or url_for('index')
	print next
	return redirect(next)

@app.route('/echo_url')
def echo_url():
	print request.path, '1111'
	print request.script_root, '22222'
	print request.url, '33333'
	print request.url_root, '5555'
	return request.base_url

if __name__ == '__main__':
	app.run()