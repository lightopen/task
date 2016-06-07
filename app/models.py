from . import db


class Image(db.Model):
    __tablename__ = "images"
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(128))


class Value(db.Model):
    __tablename__ = "values"
    id = db.Column(db.Integer, primary_key=True)
    a1 = db.Column(db.String(64))
    a2 = db.Column(db.String(64))
    a3 = db.Column(db.String(64))
    a4 = db.Column(db.String(64))
    a5 = db.Column(db.String(64))
    a6 = db.Column(db.String(64))
    a7 = db.Column(db.String(64))
    a8 = db.Column(db.String(64))
    a9 = db.Column(db.String(64))
    a10 = db.Column(db.String(64))
    a11 = db.Column(db.String(64))
    a12 = db.Column(db.String(64))
    a13 = db.Column(db.String(64))
    a14 = db.Column(db.String(64))
    a15 = db.Column(db.String(64))
    image = db.Column(db.String(128))
    code = db.Column(db.String(32))
