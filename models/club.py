from db import db


class ClubModel(db.Model):
	__tablename__ = 'club'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))

	players = db.relationship('PlayerModel', lazy='dynamic')

	def __init__(self, name):
		self.name = name

	def json(self):
		return {'name': self.name, 'players': [player.json() for player in self.players.all()]}

	@classmethod
	def find_club(cls, name):
		return cls.query.filter_by(name=name).first()
		

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()
