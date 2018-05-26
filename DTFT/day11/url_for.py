from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def f_root():
	pass

@app.route('/indestry')
def f_industry():
	pass

@app.route('/book/<book_name>')
def f_book(book_name):
	pass

with app.test_request_context():
	print url_for('f_root', _external=True)
	print url_for('f_industry')
	print url_for('f_industry', name='web')
	print url_for('f_book', book_name='Python book')