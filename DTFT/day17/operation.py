import ER
from sqlalchemy import or_, and_

def InserClass(name, level, address):
	with ER.session_scope() as session:
		classes = ER.Class(name=name, level=level, address=address)
		session.add(classes)

def GetClass(class_id=None, name=None):
	with ER.session_scope() as session:
		return session.query(ER.Class).filter(
			or_(ER.Class.class_id == class_id, ER.Class.name == name)).first()

def DeleteClass(name):
	with ER.session_scope() as session:
		classes = GetAccount(name=name)
		if classes:
			session.delete(classes)

def UpdateClass(class_id, name, level, address):
	with ER.session_scope() as session:
		classes = session.query(ER_Class).filter(ER_Class.class_id == class_id)
		if not classes: return 
		classes.name = name
		classes.level = level
		classes.address = address

def InserStudent(name, age, gender, address, class_id):
	with ER.session_scope() as session:
		student = ER.Student(name=name, age=age, gender=gender, address=address, class_id=class_id)
		session.add(student)

def GetStudent(student_id=None, name=None):
	with ER.session_scope() as session:
		return session.query(ER.Student).filter(
			or_(ER.Student.student_id == student_id, ER.Student.name == name)).first()

def DeleteStudent(name):
	with ER.session_scope() as session:
		student = GetStudent(name=name)
		if student:
			session.delete(student)

def UpdateStudent(student_id, name, age, gender, address, class_id):
	with ER.session_scope() as session:
		student = session.query(ER_Student).filter(ER_Student.student_id == student_id)
		if not student: return 
		student.name = name
		student.age = age
		student.gender = gender
		student.address = address
		student.class_id = class_id

def InserTeacher(name, gender, telephone, address):
	with ER.session_scope() as session:
		teacher = ER.Teacher(name=name, gender=gender, telephone=telephone, address=address)
		session.add(teacher)

def GetTeacher(teacher_id=None, name=None):
	with ER.session_scope() as session:
		return session.query(ER.Teacher).filter(
			or_(ER.Teacher.teacher_id == teacher_id, ER.Teacher.name == name)).first()

def DeleteTeacher(name):
	with ER.session_scope() as session:
		teacher = GetTeacher(name=name)
		if teacher:
			session.delete(teacher)

def UpdateTeacher(teacher_id, name, gender, telephone, address):
	with ER.session_scope() as session:
		teacher = session.query(ER_Teacher).filter(ER_Teacher.teacher_id == teacher_id)
		if not teacher: return 
		teacher.name = name
		teacher.gender = gender
		teacher.telephone = telephone
		teacher.address = address

def InserClassTeacher(teacher_id, class_id):
	with ER.session_scope() as session:
		classteacher = ER.ClassTeacher(teacher_id=teacher_id, class_id=class_id)
		session.add(classteacher)

def GetClassTeacher(teacher_id=None, class_id=None):
	with ER.session_scope() as session:
		return session.query(ER.ClassTeacher).filter(
			or_(ER.ClassTeacher.teacher_id == teacher_id, ER.ClassTeacher.class_id == class_id)).first()

def DeleteClassTeacher(teacher_id,class_id):
	with ER.session_scope() as session:
		classteacher = GetClassTeacher(teacher_id=teacher_id,class_id=class_id)
		if classteacher:
			session.delete(classteacher)

def UpdateClassTeacher(teacher_id, class_id):
	with ER.session_scope() as session:
		teacher = session.query(ER_ClassTeacher).filter(ER_ClassTeacher.teacher_id == teacher_id)
		if teacher:
			classteacher.class_id = class_id
		else:
			classes = session.query(ER_ClassTeacher).filter(ER_ClassTeacher.class_id == class_id)
			if classes:
				classteacher.teacher_id = teacher_id
			else:
				pass