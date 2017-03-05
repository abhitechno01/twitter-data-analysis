__author__ = 'Gagan Brar'
import pygraphviz as pgv
from pymongo import MongoClient

conn = MongoClient().followers.abhi_techno01
graph = pgv.AGraph()
for i in conn.find():
    graph.add_edge(i['user'],i['follower'])
graph.layout(prog='neato')
graph.draw('followersnet_pygraphviz_visualization.png')