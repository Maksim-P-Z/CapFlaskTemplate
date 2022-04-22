from app import app, login
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Fact
from app.classes.forms import FactForm
from flask_login import login_required
import datetime as dt

@app.route('/fact/new')
def factNew():
    pass
