from flask import Flask
from def_form import BulletinForm
from flask import render_template
from flask import request

app = Flask(__name__)
app.config['SECRET_KEY']='123'
@app.route('/bd/view_bulletins', methods=['GET', 'POST'])
def view_bulletins():
	form =BulletinForm(request.form)
	return render_template('view_bulletin.html', form=form)

if __name__ == '__main__':
	app.run()