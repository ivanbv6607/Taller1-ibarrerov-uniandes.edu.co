from flask_login import UserMixin
from config.db import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    es_admin = db.Column(db.Boolean, nullable=False)
    genero = db.Column(db.String(10), nullable=False)