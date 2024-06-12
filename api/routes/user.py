# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

# Create a new Flask application
app = Flask(__name__)

# Configure the database URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Initialize the Marshmallow object
ma = Marshmallow(app)

# Enable cross-origin resource sharing (CORS) for the application
CORS(app)

# Define the User model
class User(db.Model):
    # Define the primary key as an integer
    id = db.Column(db.Integer, primary_key=True)
    
    # Define the username as a string with a maximum length of 80, unique, and not nullable
    username = db.Column(db.String(80), unique=True, nullable=False)
    
    # Define the password as a string with a maximum length of 120
    password = db.Column(db.String(120), nullable=False)

    # Define the constructor for the User model
    def __init__(self, username, password):
        # Initialize the attributes of the User model
        self.username = username
        self.password = password

# Define the UserSchema for serializing and deserializing User objects
class UserSchema(ma.Schema):
    class Meta:
        # Define the fields to include in the schema
        fields = ("id", "username", "password")

# Create instances of the UserSchema for serialization and deserialization
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Define API routes
@app.route("/api/user", methods=["GET"])
def get_user():
    # Fetch the user based on the provided ID
    user = User.query.get(request.args.get("id"))
    
    # Check if the user exists
    if user is None:
        # Return an error message with a 404 status code
        return jsonify({"error": "User not found"}), 404
    
    # Return the user in JSON format
    return jsonify(user_schema.dump(user))

@app.route("/api/user", methods=["POST"])
def create_user():
    # Extract the username and password from the JSON request
    username = request.json["username"]
    password = request.json["password"]
    
    # Create a new User object
    new_user = User(username, password)
    
    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    
    # Return the new user in JSON format with a 201 status code
    return jsonify(user_schema.dump(new_user)), 201

@app.route("/api/user", methods=["PUT"])
def update_user():
    # Fetch the user based on the provided ID
    user = User.query.get(request.args.get("id"))
    
    # Check if the user exists
    if user is None:
        # Return an error message with a 404 status code
        return jsonify({"error": "User not found"}), 404
    
    # Update the username and password of the user
    user.username = request.json["username"]
    user.password = request.json["password"]
    
    # Commit the changes to the database
    db.session.commit()
    
    # Return the updated user in JSON format
    return jsonify(user_schema.dump(user))

@app.route("/api/user", methods=["DELETE"])
def delete_user():
    # Fetch the user based on the provided ID
    user = User.query.get(request.args.get("id"))
    
    # Check if the user exists
    if user is None:
        # Return an error message with a 404 status code
        return jsonify({"error": "User not found"}), 404
    
    # Delete the user from the database
    db.session.delete(user)
    db.session.commit()
    
    # Return a success message
    return jsonify({"message": "User deleted"})

# Run the application in debug mode if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
