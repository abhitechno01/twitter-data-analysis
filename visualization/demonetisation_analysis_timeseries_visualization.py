__author__ = 'Gagan Brar'
import pandas
import vincent
from pymongo import MongoClient

'''
here for each visualization it creates two files
1. json file that contains actual data set
2. html file that implements the json file
to visualize the vega scaffold, one need to run a server and then open the html file
'''

conn = MongoClient().test_database.pmmodi

dates_support = []
dates_iamwithmodi = []
dates_against = []
i =0
for data in conn.find():
    i = i+1
    if i==60000:
        break
    print i
    if 'support' in data['Tweet']:
        dates_support.append(data['Tweet created at'])
    if 'iamwithmodi' in data['Tweet']:
        dates_iamwithmodi.append(data['Tweet created at'])
    if 'against' in data['Tweet']:
        dates_against.append(data['Tweet created at'])

print len(dates_support)
print len(dates_iamwithmodi)
print len(dates_against)
ones_s = [1]*len(dates_support)
ones_i = [1]*len(dates_iamwithmodi)
ones_a = [1]*len(dates_against)

# the index of the series
idx_s = pandas.DatetimeIndex(dates_support)
idx_i = pandas.DatetimeIndex(dates_iamwithmodi)
idx_a = pandas.DatetimeIndex(dates_against)
# the actual series (at series of 1s for the moment)
support = pandas.Series(ones_s, index = idx_s)
iamwithmodi = pandas.Series(ones_i, index=idx_i)
against = pandas.Series(ones_a, index=idx_a)

# resampling
per_minute_s = support.resample('1Min').sum().fillna(0)
per_minute_i = iamwithmodi.resample('1Min').sum().fillna(0)
per_minute_a = against.resample('1Min').sum().fillna(0)

#all data together
t_data = dict(IAMWITHMODI = per_minute_i,SUPPORT = per_minute_s, AGAINST = per_minute_a)
all_three = pandas.DataFrame(data = t_data, index=per_minute_a.index)
all_three = all_three.resample('1Min').sum().fillna(0)


time_chart = vincent.Line(all_three[['SUPPORT','IAMWITHMODI','AGAINST']])
time_chart.axis_titles(x='Time', y='Freq')
time_chart.legend(title='Matches')
time_chart.to_json('time_chart4.json',html_out=True, html_path='time_chart4.html')

