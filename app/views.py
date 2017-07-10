"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, flash, redirect, request\
                  ,session,url_for,g, jsonify
from app import application,db,models
from .forms import LoginForm

from flask_login import LoginManager, UserMixin, \
                  login_required, login_user, logout_user ,current_user 

login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = "login"

@application.before_request
def before_request():
    g.user = current_user

@login_manager.user_loader
def load_user(id):
    return models.User.query.get(int(id))


@application.route('/login', methods=['GET', 'POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        remember_me = False
        if 'remember_me' in request.form:
            remember_me = True
        registered_user = models.User.query.filter_by(username=username,password=password).first()
        if registered_user is None:
            flash('Username or Password is invalid' , 'error')
            return redirect(url_for('login'))
        login_user(registered_user, remember = remember_me)
        flash('Logged in successfully')
        return redirect('/home')
   return render_template('login.html', title='Sign In', form=form)

@application.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@application.route('/')
@application.route('/home')
@login_required
def home():
    """Renders the home page."""
    return render_template('index.html', title='Home Page', year=datetime.now().year)

    

