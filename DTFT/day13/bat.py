from werkzeug.contrib.cache import SimpleCache
from flask import request, render_template, Flask

CACHE_TIMEOUT = 3

cache = SimpleCache()
cache.timeout = CACHE_TIMEOUT

app = Flask(__name__)

@app.before_request
def return_cached():
	if not request.values:
		response = cache.get(request.path)
		if response:
			print 'Got the page from cache'
	print 'Will load the page'

@app.after_request
def cache_response(response):
	if not request.values:
		cache.set(request.path, response, CACHE_TIMEOUT)
	return response

@app.route('/get_index')
def index():
	return render_template('jinja2.html',a_variable='Developer', navigation=['http://www.163.com','http://www.baidu.com'])
if __name__ == '__main__':
	app.run()