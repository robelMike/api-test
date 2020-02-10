import sqlite3
from flask_restful import Resource, reqparse
from models.users import ModelUser


class User():
    #TABLE_NAME = 'users'

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT *FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
        
    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


class UserRegister(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left OFF!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left good!"
                        )
    def post(self):
        datan = UserRegister.parser.parse_args()

        if ModelUser.find_by_username(datan['username']):
           return {"message": "user already exist!"}, 400

        user = ModelUser(datan['username'], datan['password'])
        user.save_to_db()

        return {"message": "user created succesfully!"}, 201
   
