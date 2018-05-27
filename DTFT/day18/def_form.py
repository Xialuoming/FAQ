#/usr/env/bin python
#-*- coding: utf-8 -*-
# from flask.ext.wtf import Form
from flask_wtf import Form
from wtforms import StringField, BooleanField, HiddenField, TextAreaField, DateTimeField, FileField
from flask_wtf.file import FileAllowed
class BaseForm(Form):
	id = HiddenField('id')
	
class BulletinForm(BaseForm):
	dt = DateTimeField(u'发布时间', format='%Y-%m-%d %H:%M:%S')
	title = StringField(u'标题')
	content = TextAreaField(u'详情')
	vaild = BooleanField(u'是否有效')
	source = StringField(u'来源')
	author = StringField(u'作者')
	image = FileField(u'上传图片',validators=[FileAllowed(['jpg', 'png'],'Images only!')])