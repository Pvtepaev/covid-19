import os
import wget


data_url = 'https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series/'
filename_recovered = 'time_series_19-covid-Recovered.csv'
filename_confirmed = 'time_series_19-covid-Confirmed.csv'
filename_deaths = 'time_series_19-covid-Deaths.csv'

os.chdir('./data/')
os.remove(filename_recovered)
os.remove(filename_confirmed)
os.remove(filename_deaths)


try:
    wget.download(data_url + filename_recovered, filename_recovered)
except:
    print('Error downloading file' + filename_recovered)
try:
    wget.download(data_url + filename_confirmed, filename_confirmed)
except:
    print('Error downloading file' + filename_confirmed)
try:
    wget.download(data_url + filename_deaths, filename_deaths)
except:
    print('Error downloading file' + filename_deaths)

