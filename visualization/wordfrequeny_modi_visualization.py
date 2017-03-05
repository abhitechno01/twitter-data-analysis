__author__ = 'Gagan Brar'
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from pymongo import MongoClient

'''
wordcloud filters most of the unwanted words e.g. as,what,are,you etc.
it gives the output in picture format(here we used jpeg)
'''

conn = MongoClient().test_database.pmmodi
text = ''
j=1
for i in conn.find():
    if j==11200:
        break
    data = i['Tweet']
    text = text + data
    print type(data)
    j = j+1
swords = set(STOPWORDS)
swords.add('https')
wc = WordCloud(background_color='white',height=768,width=1366,stopwords=swords,max_words=100).generate(text)
wc.to_file('modi2.jpeg')