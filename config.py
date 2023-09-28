import os
from flask import Flask
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app = connexion.App(__name__, specification_dir="../")
# app.add_api("swagger.yml")
db = SQLAlchemy(app)
ma = Marshmallow(app)