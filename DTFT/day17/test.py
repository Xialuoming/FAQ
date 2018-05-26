#-*- coding: utf-8 -*-
from operation import *
import ER
# InserClass('1班', 1, '芝兰路')
# InserClass('2班', 1, '龙眠大道')
# InserClass('3班', 2, '长江路')

# InserStudent('袁健', 18, '男', '梧桐语',2)
# InserStudent('杨颖', 18, '女', '梧桐语',1)

# InserTeacher('A', 'man', '1111111', '九龙湖')
# InserTeacher('B', 'man', '2222222', '小龙湾')
# InserTeacher('C', 'man', '33333', '孤岛')

# InserClassTeacher(11,11)
# InserClassTeacher(12,12)

with ER.session_scope() as session:
	class_ = session.query(ER.Class).filter(ER.Class.name=='2班')
	for student in class_.students:
		print u'姓名: %s, 年龄: %d' %(student.name,student.age)

	class_ = session.query(ER.Class).filter(ER.Class.name=='1班').first()
	for class_teacher in class_.class_teachers:
		teacher = class_teacher.teacher
		print u"姓名: %s, 电话: %s" %(teacher.name,teacher.telephone)