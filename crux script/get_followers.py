import tweepy
import time

'''
I've changed my key credential, so one need to input their key credential in order to 
make this script work smoothly. In this script, we are saving follower's list in a file
'''

ckey = 'ihH41vUuoWpYpdZ3Nfpt9fPrD'
csecret = 'O2T4MjRmx08uos1cg6iatQ0UgPSwsdPDB4uH8JNuWGYE2rlPWO'
atoken = '3491220253-96UkimCRyFlbmdaJZPf653qUTivuY4TrHTzugkC'
asecret = 'WLDqD2cgR8tPyRzJW4WKiwDLmnOjoE535ZdmEXbIiMexU'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

file= open('followerlist.txt','a')
if(api.verify_credentials):
    print 'We sucessfully logged in'

user = tweepy.Cursor(api.followers, screen_name="abhi_techno01").items()
while True:
    try:
        u = next(user)
        file.write(u.screen_name +' \n')

    except:
        time.sleep(15*60)
        print 'We got a timeout ... Sleeping for 15 minutes'
        u = next(user)
        file.write(u.screen_name +' \n')
file.close()
