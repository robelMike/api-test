from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.player import PlayerModel


class Player(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left LMFAO!"
                        )
	parser.add_argument('club_id',
                        type=int,
                        required=True,
                        help="This field cannot be left LMFAO!"
                        )


	@jwt_required()
	def get(self, name):
		item = self.find_name(name)
		return item, 201


	def post(self, name):
		if PlayerModel.find_name(name):
			return {'message': "An item with name '{}' already exists.".format(name)}, 400

		data = Player.parser.parse_args()

		item = PlayerModel(name, **data)

		try:
			item.save_to_db()
		except:
			return {"message": "An error occurred inserting the item."}, 500

		return item.json(), 201

		players.append(player)
		return player
	def put(self, name):
		data = Player.parser.parse_args()
		item = PlayerModel.find_name(name)
		if item is None:
				item = PlayerModel(name, data['price'])
		else:
				item.price = data['price']
				item.save_to_db()
		return item.json()

	def delete(self, name):
		player = PlayerModel.find_name(name)

		if player:
			player.delete_from_db()
			return{"Message": "Player deleted!"}
		return{"Message": "Player not found"}
	        


@classmethod
def update(cls, item):
		print("INSIDE UPDATE")
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()
		print("INSIDE UPDATE->2")
		query = "UPDATE players SET price=? WHERE name =?" 
		cursor.execute(query, (item['price'], item['name']))
		print("INSIDE UPDATE->3")
		connection.commit()
		connection.close()


class Playerlist(Resource):
	def get(self):
		return{'players': [player.json() for player in PlayerModel.query.all()]}