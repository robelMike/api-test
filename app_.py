from flask import Flask, request 
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
import sqlite3

from security_ import authenticate, identity
from resources.users_ import UserRegister
from resources.player import Player, Playerlist
from resources.club import Club, Clublist
from flask_restful import Resource, reqparse

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app.secret_key = 'mike'
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth


api.add_resource(Player, '/player/<string:name>')
api.add_resource(Club, '/club/<string:name>')
api.add_resource(Clublist, '/clubs')

api.add_resource(Playerlist, '/player')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
	from db import db
	db.init_app(app)

app.run(port=5000, debug=True)