from flask import Flask
# import orm
from sqlalchemy import orm
from flask import render_template
from flask import request, redirect, url_for
import datetime
from def_form import BulletinForm
app = Flask(__name__)
app.config['SECRET_KEY']='123'
# app.secret_key = 'SET_ME_BEFORE_USE_SESSION'

@app.route('/bd/view_bulletins', methods=['GET', 'POST'])
def view_bulletin():
	form = BulletinForm(request.form)
	if request.method == 'POST' and form.validate():
		print '1111111111111111111111'
		if form.id.data:
			bulletin = orm.bulletin.query.get(int(form.id.data))
			bulletin.dt = dorm.dt.data
			bulletin.title = form.title.data
			bulletin.content = form.content.data
			bulletin.source = form.source.data
			bulletin.author = form.author.data
			orm.db.session.commit()
		else:
			bulletin = orm.Bulletin(form.dt.data, form.title.data, form.content.data,\
				form.source.data, form.author.data)
			orm.db.session.add(bulletin)
			orm.db.session.commit()
			form.id.data = bulletin.id

		if request.form.has_key('upload'):
			file = request.files['image']
			if file:
				file_server = str(uuid.uuid1()) + Util.file_extension(file.filename)
				pathfile_server = os.path.join(UPLOAD_PATH, file_server)
				file.save(pathfile_server)
				if os.stat(pathfile_server).st.size<1*1024*1024:
					bulletinimage = orm.Bulletinimage(bulletin.id, file_server)
					orm.db.session.merge(bulletinimage)
					orm.db.session.commit()
				else:
					os.remove(pathfile_server)
			else:
				return redirect(url_for('view_bulletin'))
	else:
		form.dt.data = datetime.datetime.now()
		print '22222222222222222222222'
	if form.id.data:
		bulletin = orm.Bulletin.query.get(int(form.id.data))
		form.bulletin = bulletin
		if form.bulletin:
			form.bulletinimages = form.bulletin.bulletinimages
	return render_template('view_bulletin.html', form=form)

if __name__ == '__main__':
	app.run()