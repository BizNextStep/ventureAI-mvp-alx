from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///business_ideas.db"
db = SQLAlchemy(app)

class BusinessIdea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    industry = db.Column(db.String(100), nullable=False)
    investment_potential = db.Column(db.Float, nullable=False)

@app.route("/api/business_ideas", methods=["GET"])
def get_business_ideas():
    ideas = BusinessIdea.query.all()
    return jsonify([{"id": idea.id, "industry": idea.industry, "investment_potential": idea.investment_potential} for idea in ideas])

@app.route("/api/business_ideas", methods=["POST"])
def create_business_idea():
    data = request.get_json()
    idea = BusinessIdea(industry=data["industry"], investment_potential=data["investment_potential"])
    db.session.add(idea)
    db.session.commit()
    return jsonify({"message": "Business idea created successfully"})

if __name__ == "__main__":
    app.run(debug=True)
