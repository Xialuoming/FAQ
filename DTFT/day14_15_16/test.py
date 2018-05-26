#/usr/vin/env python
#-*- coding: utf-8 -*-
from flask import render_template, Flask

app = Flask(__name__)

@app.route('/test')
def test():
	return render_template('sub.html',site_name='super_test')

if __name__ == '__main__':
	app.run()