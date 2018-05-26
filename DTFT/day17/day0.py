AttributeError: ‘Query’ object has no attribute ‘students’

class_ = session.query(ER.Class).filter(ER.Class.name=='2班')

class_ = session.query(ER.Class).filter(ER.Class.name=='2班').first()
