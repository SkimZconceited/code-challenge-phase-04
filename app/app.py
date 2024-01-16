#!/usr/bin/env python3

import os
from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Hero

abs_path = os.getcwd()
# abs_python_path = os.path.normpath(abs_path) for windows purposes
db_path = f'sqlite:///{abs_path}/db/app.db'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return ''

@app.route("/heroes")
def heroes():
    all_heroes = Hero.query.all()
    heroes_list = [hero.to_dict() for hero in all_heroes]
    print(heroes_list)
    return jsonify(heroes_list)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
