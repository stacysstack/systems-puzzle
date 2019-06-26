import datetime
import os
import random

from flask import Flask, render_template, redirect, url_for, flash
from forms import ItemForm
from models import Items
from database import db_session
# do need to add init_db import to get database up

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']

@app.route("/", methods=('GET', 'POST'))
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        item = Items(id=random.randint(1,5000), name=form.name.data, quantity=form.quantity.data, description=form.description.data, date_added=datetime.datetime.now())
        db_session.add(item)
        db_session.commit()
        flash('Thank you for entering your item')
        return redirect(url_for('success'))
    # else: add some sort of error catching here

    return render_template('index.html', form=form)

@app.route("/success")
def success():
    # results = []
    # qry = db_session.query(Items)
    # results = qry.all()
    # return str(results)
  
    return str(Items.query.all())

if __name__ == '__main__':
    ## add port here maybe? (host= '0.0.0.0', port=5001) 
    ## by default flask runs on 5000
    # init_db()
    app.run(host='0.0.0.0', port=5001, debug=True)
