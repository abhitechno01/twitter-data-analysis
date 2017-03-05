
import tweepy
import pymongo

def getFollowers(s_name):
    '''
    function takes a target user name against which you desire
    followers and saves the content in a dictionary and writes
    this dictionary in a mongoDB database. 
    '''
    count = 0
    f = open('followers_net.txt','a')
    for userObj in tweepy.Cursor(api.followers, screen_name =s_name).items(200):
        strfyUser = str(userObj.screen_name)
        data = {
            'user' : s_name,
            'follower' : strfyUser
        }
        f.write('{'+s_name+' : '+strfyUser+'}\n')
        conn.insert(data)
        print data
        count = count + 1
    f.write('\n')
    f.close()
    return count


ckey = 'ihH41vUuoWpYpdZ3Nfpt9fPrD'                             #inset your token credential otherwise script fails
csecret = 'O2T4MjRmx08uos1cg6iatQ0UgPSwsdPDB4uH8JNuWGYE2rlPWO'
atoken = '3491220253-96UkimCRyFlbmdaJZPf653qUTivuY4TrHTzugkC'
asecret = 'WLDqD2cgR8tPyRzJW4WKiwDLmnOjoE535ZdmEXbIiMexU'

conn = pymongo.MongoClient().followers.abhi_techno01 #creating collection "followers" and document "abhi_techno01"
conn.remove()                                        #removes any pre-saved content on abhi_techno01

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
if(api.verify_credentials):
    print 'We sucessfully logged in'
s_name = raw_input('Input twitter handler (e.g. TimesNow)')
docCount = getFollowers(s_name)
count  = 1
for i in conn.find():
    if (count <= docCount):
        followerName = i['follower']
        getFollowers(followerName)
    else:
        break
    count = count + 1