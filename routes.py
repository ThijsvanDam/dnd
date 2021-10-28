# routes.py

from flask import render_template
from app import app
from app.models import User
from app.forms import <your-form>

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/user',methods=["GET"])
def signup():
    # ...
    user = User.query.filter_by(username=form.username.data)