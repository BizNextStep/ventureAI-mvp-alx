import os
import json
from flask import Flask, request, jsonify
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_FILE_DIR"] = os.path.join(app.root_path, "sessions")
Session(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "password")

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route("/user", methods=["GET"])
def get_user():
    user = User.query.get(request.args.get("id"))
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user_schema.dump(user))

@app.route("/user", methods=["POST"])
def create_user():
    username = request.json["username"]
    password = request.json["password"]
    user = User(username, password)
    db.session.add(user)
    db.session.commit()
    return jsonify(user_schema.dump(user)), 201

@app.route("/user", methods=["PUT"])
def update_user():
    user = User.query.get(request.args.get("id"))
    if user is None:
        return jsonify({"error": "User not found"}), 404
    user.username = request.json["username"]
    user.password = request.json["password"]
    db.session.commit()
    return jsonify(user_schema.dump(user))

@app.route("/user", methods=["DELETE"])
def delete_user():
    user = User.query.get(request.args.get("id"))
    if user is None:
        return jsonify({"error": "User not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"})

if __name__ == "__main__":
    app.run(debug=True)
