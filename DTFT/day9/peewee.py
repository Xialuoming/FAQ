# !usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *

db = SqliteDatabase("sampleDB.db")

class BaseModel(Model):
	class Meta:
		database = db

class Course(BaseModel):
	id = PrimaryKeyField()
	title = CharField(null = False)
	period = IntegerField()
	description = CharField()
	class Meta:
		order_by = ('title',)
		db_table = 'course'

class Teacher(BaseModel):
	id = PrimaryKeyField()
	name = CharField(null = False)
	gender = BooleanField()
	address = CharField()
	course_id = ForeignKeyField(Course, to_field = 'id', related_name = "course")
	class Meta:
		order_by = ('name',)
		db_table = 'teacher'
Course.drop_table()
Teacher.drop_table()
Course.create_table()
Teacher.create_table()
Course.create(id = 1, title = '经济学', period = 320, description = '文理科均可选修课')
Course.create(id = 2, title = '大学英语', period = 300, description = '大一必修课')
Course.create(id = 3, title = '哲学', period = 100, description = '必修课')
Course.create(id = 104, title = '编译原理', period = 100, description = '计算机选修课')
Teacher.create(name = '赵', gender = True, address = '...', course_id = 1)
Teacher.create(name = '钱', gender = True, address = '///', course_id = 3)
Teacher.create(name = '孙', gender = False, address = '///', course_id = 2)

record = Course.get(Course.title=='大学英语')
print record.title,record.period,'0'

record.period = 200
record.save()
record = Course.get(Course.title=='大学英语')
print record.title,record.period,'1'

record.delete_instance()
# record = Course.get(Course.title=='大学英语')
print record.title,record.period,'2'

courses = Course.select()

courses = Course.select().where(Course.id < 10).order_by(Course.period.desc())

total = Course.select(fn.Avg(Course.period).alias('avg_period'))

Course.update(period = 300).where(Course.id > 100).execute()
record = Course.get(Course.title=='编译原理')
print record.title,record.period,'3'

Record = Course.select().join(Teacher).where(Teacher.gender == True)

print Course.get(Course.id == 1)

Course.drop_table()
Teacher.drop_table()