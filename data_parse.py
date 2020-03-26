import os
import csv
from datetime import datetime, date, time
from time import strptime

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

def prepare_confirmed(ddict, dict_name):
    for i in ddict.keys():
        date = datetime.strptime(i, '%m/%d/%y')
        confirmed = ddict.get(i)
        dict_name.append({'date': str(date.date()), 'recovered': "0", \
            'confirmed': confirmed})

def write_data(file, data_list):
    with open(file, "w") as wfile:
        fieldnames = ['date', 'confirmed', 'recovered']

        writer = csv.DictWriter(wfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_list)


os.chdir('/home/loki/python/covid/data')

filename_recovered = 'time_series_covid19_recovered_global.csv'
filename_confirmed = 'time_series_covid19_confirmed_global.csv'
filename_deaths = 'time_series_covid19_deaths_global.csv'


# with open(filename_recovered, "r") as file:
#     reader = csv.DictReader(file, delimiter=',')
#     for row in reader:
#         if row['Country/Region'] == 'China' and row['Province/State'] == 'Hubei':
#             hubei_dict = row
#         elif row['Country/Region'] == 'Italy':
#             italy_dict = row
#         elif row['Country/Region'] == 'Germany':
#             germany_dict = row
#         elif row['Country/Region'] == 'US' and row['Province/State'] == 'New York':
#             newyork_dict = row
#         elif row['Country/Region'] == 'Netherlands' and row['Province/State'] == '':
#             holand_dict = row
#         elif row['Country/Region'] == 'Spain':
#             spain_dict = row

with open(filename_confirmed, "r") as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        if row['Country/Region'] == 'China' and row['Province/State'] == 'Hubei':
            hubei_dict_conf = row
        elif row['Country/Region'] == 'Italy':
            italy_dict_conf = row
        elif row['Country/Region'] == 'Germany':
            germany_dict_conf = row
        # elif row['Country/Region'] == 'US' and row['Province/State'] == 'New York':
        #     newyork_dict_conf = row
        elif row['Country/Region'] == 'Netherlands' and row['Province/State'] == '':
            holand_dict_conf = row
        elif row['Country/Region'] == 'Spain':
            spain_dict_conf = row

# clear_dict(hubei_dict, hubei_data)
clear_dict(hubei_dict_conf, hubei_data)
# clear_dict(italy_dict, italy_data)
clear_dict(italy_dict_conf, italy_data)
# clear_dict(germany_dict, germany_data)
clear_dict(germany_dict_conf, germany_data)
# clear_dict(newyork_dict, newyork_data)
# clear_dict(newyork_dict_conf, newyork_data)
# clear_dict(holand_dict, holand_data)
clear_dict(holand_dict_conf, holand_data)
# clear_dict(spain_dict, spain_data)
clear_dict(spain_dict_conf, spain_data)

# prepare_data(hubei_dict, hubei_dict_conf, hubei_data)
# prepare_data(italy_dict, italy_dict_conf, italy_data)
# prepare_data(germany_dict, germany_dict_conf, germany_data)
# prepare_data(newyork_dict, newyork_dict_conf, newyork_data)
# prepare_data(holand_dict, holand_dict_conf, holand_data)
# prepare_data(spain_dict, spain_dict_conf, spain_data)

prepare_confirmed(hubei_dict_conf, hubei_data)
prepare_confirmed(italy_dict_conf, italy_data)
prepare_confirmed(germany_dict_conf, germany_data)
# prepare_confirmed(newyork_dict_conf, newyork_data)
prepare_confirmed(holand_dict_conf, holand_data)
prepare_confirmed(spain_dict_conf, spain_data)


os.chdir('/home/loki/docker/nginx-proxy/html/data')

write_data('hubei.csv', hubei_data)
write_data('italy.csv', italy_data)
write_data('spain.csv', spain_data)
write_data('germany.csv', germany_data)
write_data('newyork.csv', newyork_data)
write_data('holand.csv', holand_data)
