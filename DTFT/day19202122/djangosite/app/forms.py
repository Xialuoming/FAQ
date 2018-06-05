#-*- coding: utf-8 -*-
from django.forms import ModelForm
from app.models import Moment
from django.forms import ValidationError

class MomentForm(ModelForm):
	class Meta:
		model = Moment
		fields = '__all__'

	def clean(self):
		cleaned_data = super(MomentForm, self).clean()
		content = cleaned_data.get("content")
		if content is None:
			raise ValidationError(u"请输入Content内容")
		elif content.find("ABCD")>=0:
			raise ValidationError(u'不能输入敏感字ABCD')
		return cleaned_data