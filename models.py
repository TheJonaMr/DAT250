from app import db
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine

key = os.environ.get("ENCRYPTION_KEY")

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(EncryptedType(db.Integer, key, AesEngine, 'oneandzeroes'), unique=True, nullable=False)
    email = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=True, nullable=False)
    fname = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=False)
    mname = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=True)
    lname = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=False)
    phone_num = db.Column(EncryptedType(db.Integer, key, AesEngine, 'oneandzeroes'), unique=False, nullable=False)
    dob = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=False)
    city = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=False)
    postcode = db.Column(EncryptedType(db.Integer, key, AesEngine, 'oneandzeroes'), unique=False, nullable=False)
    address = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=False)
    hashed_password = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=True)
    salt = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=True)
    verification_code = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=True, nullable=True)
    verified = db.Column(EncryptedType(db.Boolean, key, AesEngine, 'zeroes'), unique=False, nullable=False)
    password_reset_code = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=True, nullable=True)
    secret_key = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=True, nullable=True)
    failed_logins = db.Column(EncryptedType(db.Integer, key, AesEngine, 'oneandzeroes'), unique=False, nullable=False)
    blocked_login_until = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=True)
    last_password_reset_request = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=False)


class Blacklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=True, nullable=False)
    last = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=False)                        # Sist gang en request ble gjort
    last_bad_login = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=False)  
    # start = db.Column(db.String, unique=False, nullable=False)                       # Når det begynte å bli for mange requests
    frequent_request_count = db.Column(EncryptedType(db.Integer, key, AesEngine, 'oneandzeroes'), unique=False, nullable=False)     # Hvor mange ganger brukeren har sent for hyppige requests
    wrong_password_count = db.Column(EncryptedType(db.Integer, key, AesEngine, 'oneandzeroes'), unique=False, nullable=False)       # Hvor mange ganger brukeren har skrevet inn feil passord
    blocked_until = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=True)
    blocked_login_until = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=True)
    reason = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=True)                      


class Cookies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(EncryptedType(db.Integer, key, AesEngine, 'oneandzeroes'), unique=False, nullable=False)
    ip = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=False)
    session_cookie = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=True, nullable=False)
    valid_to = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=False)


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(EncryptedType(db.Integer, key, AesEngine, 'oneandzeroes'), unique=False, nullable=False)
    balance = db.Column(EncryptedType(db.Integer, key, AesEngine, 'oneandzeroes'), unique=False, nullable=False)
    account_number = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=True, nullable=False)
    account_name = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=False)


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transfer_time = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=False)
    from_acc = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=False)
    to_acc = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=False)
    message = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=False)
    amount = db.Column(EncryptedType(db.Integer, key, AesEngine, 'oneandzeroes'), unique=False, nullable=False)


class CommonPasswords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(EncryptedType(db.String, key, AesEngine, 'pkcs5'), unique=False, nullable=False)
