# Import the SQLAlchemy library for database operations
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object
db = SQLAlchemy()

# Define the BusinessIdea model
class BusinessIdea(db.Model):
    # Define the primary key as an integer
    id = db.Column(db.Integer, primary_key=True)
    
    # Define the title of the business idea as a string with a maximum length of 100
    title = db.Column(db.String(100), nullable=False)
    
    # Define the description of the business idea as a text field
    description = db.Column(db.Text, nullable=False)
    
    # Define the industry of the business idea as a string with a maximum length of 50
    industry = db.Column(db.String(50), nullable=False)
    
    # Define the investment potential of the business idea as a string with a maximum length of 50
    investment_potential = db.Column(db.String(50), nullable=False)
    
    # Define the user who submitted the business idea as a foreign key referencing the User model
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Define a relationship between the BusinessIdea and User models
    user = db.relationship('User', backref=db.backref('business_ideas', lazy='dynamic'))
    
    # Define the timestamp for when the business idea was created
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    
    # Define the timestamp for when the business idea was last updated
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    # Define a string representation of the BusinessIdea model
    def __repr__(self):
        return f"<BusinessIdea(id={self.id}, title='{self.title}')>"
