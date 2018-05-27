AttributeError: ‘Query’ object has no attribute ‘students’
class_ = session.query(ER.Class).filter(ER.Class.name=='2班')

class_ = session.query(ER.Class).filter(ER.Class.name=='2班').first()

SyntaxError: "keyword can't be an expression"
students = session.query(ER.Student).join(ER.Class).filter(ER.Class.level=2).all()

students = session.query(ER.Student).join(ER.Class).filter(ER.Class.level==2).all()


'type' object has no attribute __getitem__
image = FileField('上传图片',vaildators=[FileAllowed['jpg', 'png'],'Images only!'])

image = FileField('上传图片',vaildators=[FileAllowed(['jpg', 'png'],'Images only!')])

A secret key is required to use CSRF.

app.config['SECRET_KEY']='123'