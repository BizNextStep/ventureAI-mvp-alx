from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///business_ideas.db"
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

class BusinessIdea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String, nullable=False)
    industry = db.Column(db.String(50), nullable=False)
    investment_potential = db.Column(db.String(50), nullable=False)
    submitted_by = db.Column(db.String(50), nullable=False)

    def __init__(self, title, description, industry, investment_potential, submitted_by):
        self.title = title
        self.description = description
        self.industry = industry
        self.investment_potential = investment_potential
        self.submitted_by = submitted_by

class BusinessIdeaSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "description", "industry", "investment_potential", "submitted_by")

business_idea_schema = BusinessIdeaSchema()
business_ideas_schema = BusinessIdeaSchema(many=True)

# API Routes
@app.route("/api/business_ideas", methods=["GET"])
def get_business_ideas():
    business_ideas = BusinessIdea.query.all()
    return jsonify(business_ideas_schema.dump(business_ideas))

@app.route("/api/business_ideas", methods=["POST"])
def add_business_idea():
    title = request.json["title"]
    description = request.json["description"]
    industry = request.json["industry"]
    investment_potential = request.json["investment_potential"]
    submitted_by = request.json["submitted_by"]

    new_business_idea = BusinessIdea(title, description, industry, investment_potential, submitted_by)
    db.session.add(new_business_idea)
    db.session.commit()

    return jsonify(business_idea_schema.dump(new_business_idea))

if __name__ == "__main__":
    app.run(debug=True)
