from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.club import ClubModel

class Club(Resource):

	def get(self, name):
		
		player = ClubModel.find_club(name)
		if player:
			return player.json()
		return{'message': 'User doesnt exist!'}


	def post(self, name):
		if ClubModel.find_club(name):
			print('NAME: ')
			print(name)
			return{'message': 'Club already exist!'}

		club = ClubModel(name)
		try:
			club.save_to_db()
			return{'Message': 'Club added to the list!'}

		except:
			return{'Message': 'Error..'}

		return club.json(), 201

	def delete(self, name):

		club = ClubModel.find_club(name)
		if club:
			Club.delete_from_db()
			return {'Message': 'Club deleted from database!'}


class Clublist(Resource):

	def get(self):
		return {'club': list(map(lambda x: x.json(), ClubModel.query.all()))}