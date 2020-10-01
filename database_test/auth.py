'''
import pyotp
import time
totp = pyotp.TOTP('base32secret3232')
totp.now() # => '492039'

# OTP verified for current time
totp.verify('492039') # => True
time.sleep(30)
totp.verify('492039') # => False

pyotp.totp.TOTP('JBSWY3DPEHPK3PXP').provisioning_uri(name='alice@google.com', issuer_name='Secure App')
pyotp.parse_uri('otpauth://totp/Secure%20App:alice%40google.com?secret=JBSWY3DPEHPK3PXP&issuer=Secure%20App')
'''

import qrcode
import logging
import pyotp
import os
from io import StringIO
from flask import Flask, render_template, redirect, request, flash, send_file

from user import User

app = Flask(__name__)
app.config.update(SECRET_KEY=os.environ['FLASK_SESSION_SECRET_KEY'])


@app.route('/qr/<email>')
def qr(email):
    """
    Return a QR code for the secret key associated with the given email
    address. The QR code is returned as file with MIME type image/png.
    """
    u = User.get_user(email)
    if u is None:
        return ''
    t = pyotp.TOTP(u.password)
    q = qrcode.make(t.provisioning_uri(email))
    img = StringIO()
    q.save(img)
    img.seek(0)
    return send_file(img, mimetype="image/png")


@app.route('/code/<email>')
def code(email):
    """
    Returns the one-time password associated with the given user for the
    current time window. Returns empty string if user is not found.
    """
    u = User.get_user(email)
    if u is None:
        return ''
    t = pyotp.TOTP(u.password)
    return str(t.now())


@app.route('/user/<email>')
def user(email):
    """User view page."""
    u = User.get_user(email)
    if u is None:
        return redirect('/')
    return render_template('/view.html', user=u)


@app.route('/new', methods=['GET', 'POST'])
def new():
    """New user form."""
    if request.method == 'POST':
        u = User(request.form['email'])
        if u.save():
            return render_template('/created.html', user=u)
        else:
            flash('Invalid email or user already exists.', 'danger')
            return render_template('new.html')
    else:
        return render_template('new.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login form."""
    if request.method == 'POST':
        u = User.get_user(request.form['email'])
        if u is None:
            flash('Invalid email address.', 'danger')
            return render_template('login.html')
        else:
            otp = request.form['otp']
            if u.authenticate(otp):
                flash('Authentication successful!', 'success')
                return render_template('/view.html', user=u)
            else:
                flash('Invalid one-time password!', 'danger')
                return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/')
def main():
    return render_template('index.html')




''' Kilder:

https://sahandsaba.com/two-step-verification-using-python-pyotp-qrcode-flask-and-heroku.html
https://github.com/sahands/python-totp
https://github.com/pyauth/pyotp
https://github.com/neocotic/qrious
https://github.com/pyauth/pyotp
https://github.com/tadeck/onetimepass
https://stackoverflow.com/questions/8529265/google-authenticator-implementation-in-python

'''