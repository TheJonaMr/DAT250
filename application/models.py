from app import db
from flask_sqlalchemy import SQLAlchemy


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    fname = db.Column(db.String, unique=False, nullable=False)
    mname = db.Column(db.String, unique=False, nullable=True)
    lname = db.Column(db.String, unique=False, nullable=False)
    phone_num = db.Column(db.Integer, unique=True, nullable=False)
    dob = db.Column(db.String, unique=False, nullable=False)
    city = db.Column(db.String, unique=False, nullable=False)
    postcode = db.Column(db.Integer, unique=False, nullable=False)
    address = db.Column(db.String, unique=False, nullable=False)
    hashed_password = db.Column(db.String, unique=False, nullable=True)
    salt = db.Column(db.String, unique=False, nullable=True)
    verification_code = db.Column(db.String, unique=True, nullable=True)
    verified = db.Column(db.Boolean, unique=False, nullable=False)


class Cookies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=False, nullable=False)
    session_cookie = db.Column(db.String, unique=True, nullable=False)
    valid_to = db.Column(db.String, unique=False, nullable=False)


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    balance = db.Column(db.Integer, unique=True, nullable=False)
    account_number = db.Column(db.String, unique=True, nullable=False)


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tittel = db.Column(db.String, unique=True, nullable=False)
    dato = db.Column(db.String, unique=True, nullable=False)
    tidspunkt = db.Column(db.Integer, unique=True, nullable=False)

    


        