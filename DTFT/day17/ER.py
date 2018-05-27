from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Class(Base):
	__tablename__ = 'class'
	class_id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50))
	level = Column(Integer)
	address = Column(String(50))

	class_teachers = relationship("ClassTeacher",backref='class')
	students = relationship("Student", backref='class', cascade='delete')


class Student(Base):
	__tablename__ = 'student'
	student_id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50))
	age = Column(Integer)
	gender = Column(String(10))
	address = Column(String(50))
	class_id = Column(Integer, ForeignKey('class.class_id'))

class Teacher(Base):
	__tablename__ = 'teacher'
	teacher_id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50))
	gender = Column(String(10))
	telephone = Column(String(50))
	address = Column(String(50))

	class_teachers = relationship("ClassTeacher", backref = 'teacher')

class ClassTeacher(Base):
	__tablename__ = 'class_teacher'
	teacher_id = Column(Integer, ForeignKey('teacher.teacher_id'), primary_key=True)
	class_id = Column(Integer, ForeignKey('class.class_id'), primary_key=True)

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

db_connect_string = 'mysql://root:root123@127.0.0.1:3306/yuanjian?charset=utf8'
engine = create_engine(db_connect_string)
Base.metadata.create_all(engine)
SessionType = scoped_session(sessionmaker(bind=engine))

def GetSession():
	return SessionType()

from contextlib import contextmanager

@contextmanager
def session_scope():
	session = GetSession()
	try:
		yield session
		session.commit()
	except:
		session.rollback()
		raise
	finally:
		session.close()
