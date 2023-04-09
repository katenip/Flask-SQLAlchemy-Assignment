# TODO - Create SQLAlchemy DB and Movie model
from sqlalchemy import Column, Integer, String
from app import db
class Movie(db.Model):
    
        
    __tablename__ = "movie"
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    director = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer)
    def __repr__(self):
        return '<Movie %r>' % self.title