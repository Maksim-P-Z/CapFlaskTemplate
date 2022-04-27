from cmath import log
from app import app, login
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Fact
from app.classes.forms import FactForm
from flask_login import login_required
import datetime as dt

@app.route('/fact/new', methods=['GET',"POST"])
@login_required

def factNew():
    form = FactForm()
    
    if form.validate_on_submit():
        newFact = Fact(
            title = form.title.data,
            author = current_user.id,
            modifyDate = dt.datetime.utcnow,
            blurb = form.blurb.data,
            information = form.information.data,
            ## photo = 
            ## media = 
            ## votes =  
            ## comment = 
        )
        newFact.save()
        return redirect(url_for('fact',factId=newFact.id))

    return render_template("factform.html", form=form)

@app.route('/fact/new/<factId>')
@login_required

def fact(factId):
    thisFact = Fact.objects.get(id = factId)
    return render_template('fact.html', fact = thisFact)

@app.route('/fact/delete/<factId>')
@login_required
def factDelete(factId):
    deleteFact = Fact.objects.get(id = factId)
    flash(f"Deleteing fact named {deleteFact.title}.")
    deleteFact.delete()
    return redirect(url_for('factList'))

@app.route('/fact/list')
@login_required
def factList():
    factList = Fact.objects()
    return render_template('fact.html', facts=factList)