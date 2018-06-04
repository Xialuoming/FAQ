# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#新增元组用于设置消息类枚举项
KIND_CHOICES = (
	('Python技术','Python技术'),
	('数据库技术','数据库技术'),
	('经济学','经济学'),
	('文本资讯','文本资讯'),
	('个人心情','个人心情'),
	('其他','其他'),
)
# Create your models here.
class Moment(models.Model):
	content = models.CharField(max_length=200)
	user_name = models.CharField(max_length=50, default='匿名')
	kind = models.CharField(max_length=20, choices=KIND_CHOICES, 
							default=KIND_CHOICES[0])	