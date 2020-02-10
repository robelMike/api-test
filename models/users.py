from db import db

class ModelUser(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String (80))
	password = db.Column(db.String (80))

	def __init__(self, username, password):
		self.username = username
		self.password = password

	@classmethod
	def find_by_username(cls, username):
		return cls.query.filter_by(username=username).first()
        
	def find_by_id(cls, _id):
		return cls.query.filter_by(_id=_id).first() #"SELECT * FROM users WHERE id=?"


	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def delete_from_db(cls, username, password):
		User1= User(username, password)
		db.session.delete(User1)
		db.session.commit(User1)    	

