__author__ = 'Gagan Brar'
from tweepy import Stream
import tweepy

ckey = 'ihH41vUuoWpYpdZ3Nfpt9fPrD'
csecret = 'O2T4MjRmx08uos1cg6iatQ0UgPSwsdPDB4uH8JNuWGYE2rlPWO'
atoken = '3491220253-96UkimCRyFlbmdaJZPf653qUTivuY4TrHTzugkC'
asecret = 'WLDqD2cgR8tPyRzJW4WKiwDLmnOjoE535ZdmEXbIiMexU'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

id = []
for i in tweepy.Cursor(api.user_timeline, screen_name = 'abhi_techno01').pages():
    id.extend(i)

print(id)
