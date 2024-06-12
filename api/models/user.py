# Import necessary libraries
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the SQLAlchemy object
db = SQLAlchemy()

# Define the User model
class User(db.Model):
    # Define the primary key as an integer
    id = db.Column(db.Integer, primary_key=True)
    
    # Define the username as a string with a maximum length of 80, unique, and not nullable
    username = db.Column(db.String(80), unique=True, nullable=False)
    
    # Define the email as a string with a maximum length of 120, unique, and not nullable
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    # Define the password hash as a string with a maximum length of 100 and not nullable
    password_hash = db.Column(db.String(100), nullable=False)
    
    # Define the session ID as a string with a maximum length of 100 and nullable
    session_id = db.Column(db.String(100), nullable=True)
    
    # Define the timestamp for when the user was created
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    
    # Define the timestamp for when the user was last updated
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    # Define methods for setting and checking passwords
    def set_password(self, password):
        # Set the password hash using the generate_password_hash function
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # Check if the provided password matches the stored password hash
        return check_password_hash(self.password_hash, password)

    # Define a string representation of the User model
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"
