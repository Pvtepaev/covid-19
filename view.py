from app import app
import os
import csv
from flask import render_template, url_for


@app.route('/')
@app.route('/covid')
def covid():

    os.chdir('./data')

    filename_recovered = 'time_series_19-covid-Recovered.csv'
    filename_confirmed = 'time_series_19-covid-Confirmed.csv'
    filename_deaths = 'time_series_19-covid-Deaths.csv'

    with open(filename_recovered, "r") as file:
        reader = csv.DictReader(file, delimiter=',')



###Render template
    return render_template('covid.html')



