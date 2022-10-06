import hashlib

import peewee
from flask import render_template, Flask, request, jsonify, redirect, url_for, session, g
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from back_end.model.users.users_model import Users
from peewee import *

app = Flask(__name__)


class Regeditform(Form):
    fname = StringField('fname', validators=[
        validators.DataRequired(), validators.Length(min=4)])
    lname = StringField('lname', validators=[
        validators.DataRequired(), validators.Length(min=4)])

    email = StringField('email', validators=[validators.DataRequired()])
    address = StringField('address', validators=[validators.DataRequired()])
    phone = StringField('phone', validators=[validators.DataRequired()])
    password = PasswordField('password', validators=[validators.DataRequired()])
    cnf_password = PasswordField(
        'cnf_password ', validators=[validators.DataRequired(), validators.EqualTo('password')])
    accept = BooleanField('accept')


class LoginFrom(Form):
    lphone = StringField('lphone', validators=[validators.DataRequired(), ])
    password = PasswordField('password', validators=[validators.DataRequired()])


def Regesiter():
    print(request.form)
    if request.method == 'GET':
        return render_template('signIn.html')
    else:

        if request.form['type'] == 'register':
            form = Regeditform(request.form)
            if form.validate():
                try:
                    user = Users(first_name=form.fname.data, last_name=form.lname.data, phone=form.phone.data,
                                 email=form.email.data, address=form.address,
                                 password=hashlib.sha256(str(form.password.data).encode()).hexdigest(), type='customer')
                    print(hashlib.sha256(str(form.password.data).encode()).hexdigest())
                    print(form.password.data)
                    user.save_users()
                    return redirect(url_for('home'))
                except peewee.IntegrityError:
                    return jsonify({'message': 'duplicate email'}), 405
            else:
                for i in form.fields:
                    print(form._fields[i].errors)
                return jsonify({'message': form._fields['cnf_password'].errors[0]}), 403
        else:
            form = LoginFrom(request.form)
            if form.validate():
                user = Users.get(Users.phone == form.lphone.data)
                if user:
                    if user.password == hashlib.sha256(str(form.password.data).encode()).hexdigest():
                        session['user_id'] = user.user_id
                        return redirect(url_for('home'))
                    else:
                        return jsonify({'message': 'wrong password'}), 401
                else:
                    return jsonify({'message': 'user not found'}), 405
            else:
                for i in form.fields:
                    print(form._fields[i].errors)
                return jsonify({'message': 's'}), 403


def logout():
    session.clear()
    return redirect(url_for('home'))
