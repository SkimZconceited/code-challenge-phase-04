from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable = False)
    super_name = db.Column( db.String(255), nullable = False)
    
    hero_powers = db.relationship('HeroPower', back_populates='hero')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'super_name': self.super_name
        }
        
# add any models you may need. 
class Power(db.Model):
    __tablename__ = 'power'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable = False)
    description = db.Column(db.String(255), nullable = False)
    
    hero_powers = db.relationship('HeroPower', back_populates='power')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
        
    
class HeroPower(db.Model):
    __tablename__ = 'hero_power'

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable = False)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable = False)
    strength = db.Column(db.String(255), nullable = False)
    created_at = db.Column(db.DateTime, default = db.func.now(), nullable = False)
    updated_at = db.Column(db.DateTime, default = db.func.now(), onupdate = db.func.now(), nullable = True)
    
    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')
    
    def to_dict(self):
        return {
            'id': self.id,
            'hero_id': self.hero_id,
            'power_id': self.power_id,
            'strength': self.strength,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    