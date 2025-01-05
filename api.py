# imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

# flask app
app = Flask(__name__)
# setting up db using sqlalchemy 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
# define api with flask restful
api = Api(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"User(name = {self.name}, email = {self.email})"
    
# validating data to make sure it is what we expect using request parser
user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required = True, help="Name cannot be blank") # making sure name is of type string
user_args.add_argument('email', type=str, required = True, help="Email cannot be blank") # making sure email is of type string

# instead of getting the users data in the form of array, we format it in a form of json data
userFields = {
    'id':fields.Integer,
    'name':fields.String,
    'email':fields.String
}

# this class is for multiple users and the next one is for single users
class Users(Resource):
    @marshal_with(userFields) # shape the data you get from the get(self) function in the form defined using userFields
# this retrieves data using http get method similar to read in crud
    def get(self):
        users = UserModel.query.all() # retrieving all users from the db
        return users
    
    @marshal_with(userFields) # shape the data you post from the post(self) function in the form defined using userFields
# this creates data using http post method similar to create in crud
    def post(self):
        args = user_args.parse_args() # parse the arguments with the definition that we set on line 24 and line 25 and if it doesn't parse correctly, it will automaticaly send back a response so no need to create edge cases
        user = UserModel(name=args["name"], email=args["email"])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all() # retrieving all users from the db
        return users, 201

# this class is for single users and the previous one is for multiple users
class User(Resource):
    @marshal_with(userFields) # shape the data you get from the get(self) function in the form defined using userFields
# this retrieves data using http get method similar to read in crud but unlike the previous get(self) function this retrieves only one result where id = id
    def get(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        return user
    
    @marshal_with(userFields) # shape the data you update get from the patch(self, id) function in the form defined using userFields
# this updates data using http patch method similar to update in crud 
    def patch(self, id):
        args = user_args.parse_args() # parse the arguments with the definition that we set on line 24 and line 25 and if it doesn't parse correctly, it will automaticaly send back a response so no need to create edge cases
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        user.name = args["name"]
        user.email = args["email"]
        db.session.commit()
        return user
    
    @marshal_with(userFields) # shape the data you delete from the delete(self, id) function in the form defined using userFields
# this deletes data using http delete method similar to delete in crud where id = id
    def delete(self, id):
        args = user_args.parse_args() # parse the arguments with the definition that we set on line 24 and line 25 and if it doesn't parse correctly, it will automaticaly send back a response so no need to create edge cases
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users
    



# assigning class Esers with a url so when we send get request to our example.com/api/users/ then we should get all of the users returned to us
api.add_resource(Users, '/api/users/')
# assigning class User with a url so when we send get request to our example.com/api/users/<int:id> then we should get the user we requested returned to us
api.add_resource(User, '/api/users/<int:id>')

# setting up home route
@app.route('/')
def home():
    return '<h1>Flask Rest API</h1>'

# running the app with debug (only for dev, never for prod)
if __name__ == '__main__':
    app.run(debug=True)