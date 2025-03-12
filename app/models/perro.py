from config.db import db

class Perro(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(45), nullable= True)
    raza = db.Column(db.String(45), nullable= True)
    edad = db.Column(db.Integer, nullable= True)
    peso = db.Column(db.Numeric(5,2), nullable= True)
