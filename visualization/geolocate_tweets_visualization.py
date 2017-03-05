__author__ = 'Gagan Brar'
from pymongo import MongoClient
import json

'''
We are going to exploit "pmmodi" document for visualization.We are using leaf
for visualiztion. Output of this script is a json file that contains the geo 
datatype which is a must for visualization in leaf. Then we create an html 
file that uses this json file and insert some code to make visualization pretty.

for visualization we need two files
1. json file that contains actual data set
2. html file that implements the json file
to visualize one need to run a server and then open the html file
'''

conn = MongoClient().test_database.pmmodi1  
j=1
geo_data = {
    'type'  :   'FeatureCollection',
    'features'  :   []
}
i=0
for tweet in conn.find():
    if j==61000:                            #computational limitation
        break

    if tweet['coordinates']:
        i = i+1
        geo_json_feature = {
            'type'  :   'Feature',
            'geometry'  :   tweet['coordinates'],
            'properties'    :   {
                'text'  :   tweet['text'],
                'created_at':   tweet['created_at'],
                'user id'   :   tweet['user']['id'],
                'location'  :   tweet['user']['location']
            }
        }
        geo_data['features'].append(geo_json_feature)
        print i
    j = j+1
f = open('geo_data.json', 'w')
f.write(json.dumps(geo_data,indent = 4))
