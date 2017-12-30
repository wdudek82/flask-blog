import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(
    dict(
        DEBUG=True,
        SECRET_KEY='(u;`9&dx:ky?vIZ<BMX0;`zHc3YN/N',
        USERNAME='admin',
        PASSWORD='default',
        SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite',
        SQLALCHEMY_TRACK_MODIFICATIONS=True,
    )
)

db = SQLAlchemy(app)


# posts
from apps.posts import views
from apps.posts import models

db.create_all()