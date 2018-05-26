from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Account(Base):
	__tablename__ = u'yj'
	id = Column(Integer, primary_key=True)
	user_name = Column(String(50), nullable=False)
	password = Column(String(200), nullable=False)
	title = Column(String(50))
	salary = Column(Integer)

	def is_active(self):
		return True

	def get_id(self):
		return self.id

	def is_authenticated(self):
		return True

	def is_anonymous(self):
		return False


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

db_connect_string = 'mysql://root:root123@127.0.0.1:3306/yuanjian?charset=utf8'

ssl_args = {'ssl':{'cert':'/home//ssl/client-cert.pem',
					'key':'/home/shouse/ssl/client-key.pem',
					'ca':'/home/shouse/ssl/ca-cert.pem'}}
engine = create_engine(db_connect_string, connect_args=ssl_args)
SessionType = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))

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