# Import necessary libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

# Create a new Flask application
app = Flask(__name__)

# Configure the database URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///api.db"

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Initialize the Marshmallow object
ma = Marshmallow(app)

# Enable cross-origin resource sharing (CORS) for the application
CORS(app)
