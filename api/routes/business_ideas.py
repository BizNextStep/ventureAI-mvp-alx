# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

# Create a new Flask application
app = Flask(__name__)

# Configure the database URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///business_ideas.db"

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Initialize the Marshmallow object
ma = Marshmallow(app)

# Enable cross-origin resource sharing (CORS) for the application
CORS(app)

# Define the BusinessIdea model
class BusinessIdea(db.Model):
    # Define the primary key as an integer
    id = db.Column(db.Integer, primary_key=True)
    
    # Define the title of the business idea as a string with a maximum length of 100
    title = db.Column(db.String(100), nullable=False)
    
    # Define the description of the business idea as a string
    description = db.Column(db.String, nullable=False)
    
    # Define the industry of the business idea as a string with a maximum length of 50
    industry = db.Column(db.String(50), nullable=False)
    
    # Define the investment potential of the business idea as a string with a maximum length of 50
    investment_potential = db.Column(db.String(50), nullable=False)
    
    # Define the submitted by as a string with a maximum length of 50
    submitted_by = db.Column(db.String(50), nullable=False)

    # Define the constructor for the BusinessIdea model
    def __init__(self, title, description, industry, investment_potential, submitted_by):
        # Initialize the attributes of the BusinessIdea model
        self.title = title
        self.description = description
        self.industry = industry
        self.investment_potential = investment_potential
        self.submitted_by = submitted_by

# Define the BusinessIdeaSchema for serializing and deserializing BusinessIdea objects
class BusinessIdeaSchema(ma.Schema):
    class Meta:
        # Define the fields to include in the schema
        fields = ("id", "title", "description", "industry", "investment_potential", "submitted_by")

# Create instances of the BusinessIdeaSchema for serialization and deserialization
business_idea_schema = BusinessIdeaSchema()
business_ideas_schema = BusinessIdeaSchema(many=True)

# Define API routes
@app.route("/api/business_ideas", methods=["GET"])
def get_business_ideas():
    # Fetch all business ideas from the database
    business_ideas = BusinessIdea.query.all()
    
    # Return the business ideas in JSON format
    return jsonify(business_ideas_schema.dump(business_ideas))

@app.route("/api/business_ideas", methods=["POST"])
def add_business_idea():
    # Extract the data from the JSON request
    title = request.json["title"]
    description = request.json["description"]
    industry = request.json["industry"]
    investment_potential = request.json["investment_potential"]
    submitted_by = request.json["submitted_by"]

    # Create a new BusinessIdea object
    new_business_idea = BusinessIdea(title, description, industry, investment_potential, submitted_by)

    # Add the new business idea to the database
    db.session.add(new_business_idea)
    db.session.commit()

    # Return the new business idea in JSON format
    return jsonify(business_idea_schema.dump(new_business_idea))

# Run the application in debug mode if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
