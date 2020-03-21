import os
from app import app
from flask import render_template, url_for


@app.route('/')
@app.route('/covid')
def covid():

###Render template
    return render_template('covid.html')



