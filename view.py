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
    spain_data = []

    def clear_dict(ddict, dict_name):
        ddict.pop('Province/State')
        ddict.pop('Country/Region')
        ddict.pop('Lat')
        ddict.pop('Long')

    def prepare_data(ddict, ddict2, dict_name):
        for i in ddict.keys():
            date = datetime.strptime(i, '%m/%d/%y')
            recovered = ddict.get(i)
            confirmed = ddict2.get(i)
            dict_name.append({'date': str(date.date()), 'recovered': recovered, \
                'confirmed': confirmed})


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
            elif row['Country/Region'] == 'Spain':
                spain_dict = row

    with open(filename_confirmed, "r") as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            if row['Country/Region'] == 'China' and row['Province/State'] == 'Hubei':
                hubei_dict_conf = row
            elif row['Country/Region'] == 'Italy':
                italy_dict_conf = row
            elif row['Country/Region'] == 'Germany':
                germany_dict_conf = row
            elif row['Country/Region'] == 'US' and row['Province/State'] == 'New York':
                newyork_dict_conf = row
            elif row['Province/State'] == 'Netherlands':
                holand_dict_conf = row
            elif row['Country/Region'] == 'Spain':
                spain_dict_conf = row

    clear_dict(hubei_dict, hubei_data)
    clear_dict(hubei_dict_conf, hubei_data)
    clear_dict(italy_dict, italy_data)
    clear_dict(italy_dict_conf, italy_data)
    clear_dict(germany_dict, germany_data)
    clear_dict(germany_dict_conf, germany_data)
    clear_dict(newyork_dict, newyork_data)
    clear_dict(newyork_dict_conf, newyork_data)
    clear_dict(holand_dict, holand_data)
    clear_dict(holand_dict_conf, holand_data)
    clear_dict(spain_dict, spain_data)
    clear_dict(spain_dict_conf, spain_data)

    prepare_data(hubei_dict, hubei_dict_conf, hubei_data)
    prepare_data(italy_dict, italy_dict_conf, italy_data)
    prepare_data(germany_dict, germany_dict_conf, germany_data)
    prepare_data(newyork_dict, newyork_dict_conf, newyork_data)
    prepare_data(holand_dict, holand_dict_conf, holand_data)
    prepare_data(spain_dict, spain_dict_conf, spain_data)


###Render template
    return render_template('covid.html', h=hubei_data ,i=italy_data, g=germany_data, \
        n=newyork_data, hol=holand_data, s=spain_data)




