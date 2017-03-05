__author__ = 'Gagan Brar'
from pymongo import MongoClient
import vincent

'''
here for each visualization it creates two files
1. json file that contains actual data set
2. html file that implements the json file
to visualize the vega scaffold, one need to run a server and then open the html file
'''

conn = MongoClient().finalized.sentimentalanalysis
i=j=k=0
for data in conn.find():
    if data['Sentiment'] == 'Positive':
        i = i+1
    elif data['Sentiment'] == 'Negative':
        j = j+1
    else:
        k = k+1
t = i+j+k
pp = (i*100)/t
pn = (j*100)/t
pnl = (k*100)/t
pi = 'POSITIVE('+str(pp)+'%)'
ni = 'NEGATIVE('+str(pn)+'%)'
nli ='NEUTRAL('+str(pnl)+'%)'
a = { pi:i,
      ni:j,
      nli:k
      }
print a
pie = vincent.Pie(a)
pie.legend('SENTIMENTAL ANALYSIS')
pie.to_json('pie.json',html_out=True, html_path='pie.html')
donut = vincent.Pie(a, inner_radius = 200)
donut.legend('SENTIMENTAL ANALYSIS')
donut.to_json('donut.json',html_out=True, html_path='donut.html')
