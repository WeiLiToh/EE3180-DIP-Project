from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db   ##means from __init__.py import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        # email = str(request.form.get('email'))
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user:
            #check if the user exists and compare the password in user table with the password entered by the user
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')

        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        # email = str(request.form.get('email'))
        first_name = request.form.get('firstname')
        last_name = request.form.get('lastname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        hp = request.form.get('hp')
        role = request.form.get('role')
        department = request.form.get('department')

        user = User.query.filter_by(username=username).first()
        
        if user:
            flash('Username already exists.', category='error')

        # elif email:
        #     flash('Email already exists.', category='error')
        
        elif len(username) <5:
            flash('username must be greater than 5 characters.', category='error')

        elif len(first_name) <2:
            flash('First Name must be greater than 1 characters.', category='error')

        elif len(last_name) <2:
            flash('Last Name must be greater than 1 characters.', category='error')

        elif password1 != password2:
            flash('passwords don\'t match.', category='error')

        elif len(password1) <7:
            flash('password must be greater than 7 characters.', category='error')
        else:
            #add user to database
            new_user = User(username=username, password=generate_password_hash(password1, method='pbkdf2:sha256'), first_name=first_name, last_name=last_name, hp=hp, role=role, department=department)
            
            db.session.add(new_user)
            #commit the changes to the database
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))  
    
    return render_template("sign_up.html", user=current_user)
