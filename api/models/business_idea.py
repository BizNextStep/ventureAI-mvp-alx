from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BusinessIdea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    industry = db.Column(db.String(50), nullable=False)
    investment_potential = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('business_ideas', lazy='dynamic'))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return f"<BusinessIdea(id={self.id}, title='{self.title}')>"
