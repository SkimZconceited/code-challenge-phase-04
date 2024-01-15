#!/usr/bin/env python3

import os
from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Hero

abs_path = os.getcwd()
abs_python_path = os.path.normpath(abs_path)
db_path = f'sqlite:///{abs_path}/db/app.db'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    hero = Hero(name = 'Mojo Jojo', super_name = 'Crazy Ape')
    db.session.add(hero)
    db.session.commit()
    return 'Hero Added'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
