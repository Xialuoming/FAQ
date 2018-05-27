#-*- coding: utf-8 -*-
from operation import *
import ER
# InserClass('2班', 1, '芝兰路')
# InserClass('1班', 2, '龙眠大道')
# InserClass('1班', 3, '长江路')

# InserStudent('袁健', 18, '男', '梧桐语',2)
# InserStudent('杨颖', 18, '女', '梧桐语',1)

# InserTeacher('A', 'man', '1111111', '九龙湖')
# InserTeacher('B', 'man', '2222222', '小龙湾')
# InserTeacher('C', 'man', '33333', '孤岛')

# InserClassTeacher(11,11)
# InserClassTeacher(12,12)



# with ER.session_scope() as session:
# 	class_ = session.query(ER.Class).filter(ER.Class.name=='一年2班').first()
# 	for student in class_.students:
# 		print u'姓名: %s, 年龄: %d' %(student.name,student.age)

# 	class_ = session.query(ER.Class).filter(ER.Class.name=='二年1班').first()
# 	for class_teacher in class_.class_teachers:
# 		teacher = class_teacher.teacher
# 		print u"姓名: %s, 电话: %s" %(teacher.name,teacher.telephone)

# 	students = session.query(ER.Student).join(ER.Class).filter(ER.Class.level==2).all()
# 	for student in students:
# 		print student.name

# 	for student, class_ in session.query(ER.Student,ER.Class). \
# 	join(ER.Class).filter(ER.Class.level==2).all():
# 		print student.name, class_.name

class_ = ER.Class()
student1, student2 = ER.Student(), ER.Student()
class_.students.append(student1)
class_.students.append(student2)
with ER.session_scope() as session:
	session.add(class_)
	if student1 in session:
		print "The student1 has been added too!"

	student3 = ER.Student()
	if student3 in session:
		print "the student3 is added before append to the class_"
	class_.students.append(student3)
	if student3 in session:
		print "the student3 is added after append to the class_"

	class_ = session.query(ER.Class).filter(ER.Class.name == "三年2班").first()
	session.delete(class_)