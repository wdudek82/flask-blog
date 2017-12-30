import datetime as dt
import pytz
from project import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # author =
    title = db.Column(db.String(255), unique=True, nullable=False)
    content = db.Column(db.Text())
    # category =
    pub_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=dt.datetime.now)
    updated_at = db.Column(db.DateTime, default=dt.datetime.now, onupdate=dt.datetime.now)

    def __repr__(self):
        return '<Post %d: %r' % (self.id, self.title)
