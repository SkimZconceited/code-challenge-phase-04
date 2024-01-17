#!/usr/bin/env python3

import os
from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Hero, Power, HeroPower

abs_path = os.getcwd()
# abs_python_path = os.path.normpath(abs_path) for windows purposes
db_path = f'sqlite:///{abs_path}/db/app.db'


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return ''

@app.route('/heroes')
def heroes():
    all_heroes = Hero.query.all()
    heroes_list = [hero.to_dict() for hero in all_heroes]
    print(heroes_list)
    return jsonify(heroes_list)

@app.route('/heroes/<int:num>')
def hero(num):
    all_heroes = Hero.query.all()
    one_hero = [hero.to_dict() for hero in all_heroes if hero.id == num]
    print(one_hero)
    return jsonify(one_hero)

@app.route("/powers")
def powers():
    all_powers = Power.query.all()
    powers_list = [power.to_dict() for power in all_powers]
    print(powers_list)
    return jsonify(powers_list)

@app.route('/powers/<int:num>')
def single_power(num):
    all_powers = Power.query.all()
    one_power = [power.to_dict() for power in all_powers if power.id == num]
    print(one_power)
    return jsonify(one_power)

if __name__ == '__main__':
    app.run(host = '192.168.0.10', port=5555, debug=True)
