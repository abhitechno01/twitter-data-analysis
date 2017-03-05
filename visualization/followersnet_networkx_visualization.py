__author__ = 'Gagan Brar'
import networkx as nx
from pymongo import MongoClient
from matplotlib import pyplot as plt

conn = MongoClient().followers.abhi_techno01
g=nx.DiGraph()
GREEN = "#77DD77"
plt.figure(figsize=(22,22))
for i in conn.find():
    g.add_edge(i['user'],i['follower'])

nx.draw(g,node_color=GREEN,with_labels=True)
plt.savefig('net3nx.png')