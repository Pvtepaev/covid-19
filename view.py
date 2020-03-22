from app import app
import os
import csv
from flask import render_template, url_for
from datetime import datetime, date, time
from time import strptime


@app.route('/')
@app.route('/covid')
def covid():

    hubei_data  = []
    italy_data = []
    germany_data = []
    newyork_data = []
    holand_data = []

    def clear_dict(ddict, dict_name):
        ddict.pop('Province/State')
        ddict.pop('Country/Region')
        ddict.pop('Lat')
        ddict.pop('Long')
        for i in ddict.keys():
            date = datetime.strptime(i, '%m/%d/%y')
            value = ddict.get(i)
            dict_name.append({'date': date, 'value': value})

    
    os.chdir('/home/loki/python/covid/data')

    filename_recovered = 'time_series_19-covid-Recovered.csv'
    filename_confirmed = 'time_series_19-covid-Confirmed.csv'
    filename_deaths = 'time_series_19-covid-Deaths.csv'

    with open(filename_recovered, "r") as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            if row['Country/Region'] == 'China' and row['Province/State'] == 'Hubei':
                hubei_dict = row
            elif row['Country/Region'] == 'Italy':
                italy_dict = row
            elif row['Country/Region'] == 'Germany':
                germany_dict = row
            elif row['Country/Region'] == 'US' and row['Province/State'] == 'New York':
                newyork_dict = row
            elif row['Province/State'] == 'Netherlands':
                holand_dict = row

    clear_dict(hubei_dict, hubei_data)
    clear_dict(italy_dict, italy_data)
    clear_dict(germany_dict, germany_data)
    clear_dict(newyork_dict, newyork_data)
    clear_dict(holand_dict, holand_data)


###Render template
    return render_template('covid.html', h=hubei_data)



