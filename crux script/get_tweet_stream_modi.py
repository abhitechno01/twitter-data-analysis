__author__ = 'Gagan Brar'
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pymongo import MongoClient
import json
import time


ckey = 'ihH41vUuoWpYpdZ3Nfpt9fPrD'
csecret = 'O2T4MjRmx08uos1cg6iatQ0UgPSwsdPDB4uH8JNuWGYE2rlPWO'
atoken = '3491220253-96UkimCRyFlbmdaJZPf653qUTivuY4TrHTzugkC'
asecret = 'WLDqD2cgR8tPyRzJW4WKiwDLmnOjoE535ZdmEXbIiMexU'

connection = MongoClient('localhost', 27017)
db = connection.test_database #create collection "test_database"
coll = db.pmmodi             #create documents pmmodi

class mylistener(StreamListener):

    def on_data(self, data):
        try:
            tweet = json.loads(data)
            tweetClean = tweet["text"]
            cleanedtext = ' '.join([word for word in tweetClean.split(' ') if len(word) > 0 and word[0] !='.' and 'http' not in word])
            obj = {
                    "Tweet created at":tweet["created_at"],
                   "String id":tweet["id_str"],
                   "Tweet":cleanedtext,
                   "User id": tweet["id"],
                   'Username': tweet["user"]["name"],
                   'Screen name':tweet["user"]["screen_name"],
                   "Location":tweet["user"]["location"],
                   "User description":tweet["user"]["description"],
                   'Followers':tweet["user"]["followers_count"],
                   "Following" :tweet["user"]["friends_count"],
                   "Likes":tweet["user"]["favourites_count"],
                   "Tweet count":tweet["user"]["statuses_count"]
                    }
            print obj   
            coll.insert(obj)    #insert object in mongoDB database    
            return True

        except BaseException, e:
            print ('failed ondata,', str(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        print (status)
        return True

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, mylistener())
twitterStream.filter(track=['modi'])
