import os
from flask import Flask, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)


class Other_Information(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    ProjectID = db.Column(db.Integer, db.ForeignKey('Project.ID'), nullable=False)
    Availability = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Other_Information {self.ID}>'