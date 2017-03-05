__author__ = 'Gagan Brar'
from textblob import TextBlob as t
import tweepy
from pymongo import MongoClient

conn = MongoClient().finalized.sentimentalanalysis

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
public_tweets = api.search(q = "life", count= 100)

for tweets in public_tweets:
    tweet = tweets._json
    tweetClean = tweet['text']
    file1 = open('sentiAnaly2.json','a')
    
    if tweetClean.split()[0] == 'RT' and tweetClean.split()[1][0] =='@':
        continue
    
    cleanedtext = ' '.join([word for word in tweetClean.split(' ') if len(word) > 0 
                      and word[0] != '@' and word[0] !='.' and word[0] != '#' and 'http' not in word])
    
    analysis = t(cleanedtext)
    score =  (analysis.sentiment.polarity)*10   #sentiment function gives the result in the range of [-1,1]
    if score > 0:
        senti = "Positive"
    elif score < 0:
        senti = "Negative"
    else:
        senti = "Neutral"
    obj = { "Tweet" :   cleanedtext,
            "Score(Out of 10)"  :   score,
            "Sentiment" :   senti,
            'User ID'   :   tweet['user']['id'],
            'Twitter Handler' :   tweet['user']['screen_name']}
    file1.write(str(obj))
    conn.insert(obj)
    print obj
    file1.close()