from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import tweepy
import os
# import codecs

path_data ="C:/Users/ARKM/Desktop/BUDDY MATCHING SYSTEM FOR CONCERTS AND LIVE SHOWS/BUDDY-MATCHING-SYSTEM-FOR-CONCERTS-AND-LIVE-SHOWS/static/data"
path_user=path_data+'/user_data'
path_hastag = path_user+'/hastag'
path_user_login = path_data+'/user_login'
key=open(f'{path_data}/key.txt').read().splitlines()
consumer_key = key[0]
consumer_secret = key[1]
access_token = key[2]
access_secret = key[3]
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def crawler():
    uid=open(f'{path_user_login}/user_id.txt').read()
    
    print(uid)
    username = api.get_user(uid).screen_name
    number_of_tweets = 3000
    name = "@"+username
    tw = tweepy.Cursor(api.user_timeline, screen_name=name, tweet_mode="extended").items()
    # Number of tweets to pull
    

    # Calling the user_timeline function with our parameters
    # results = api.user_timeline(screen_name=username, count=tweetCount)

    

    print(f"visiting : {name}")
    
    count = 0
    f = open(f"{path_user_login}/user_login.txt", 'a', encoding='utf-8')
    for status in tw:
        if count >= number_of_tweets:
            break
        count += 1
        f.write(status.full_text)
    print(f"got user: {name}")
    file = open(f'{path_user_login}/user_login.txt','r', encoding='utf-8').read().split('#')
    n = open(f'{path_user_login}/get_hastag_user_login.txt', 'a', encoding="utf-8")
    for x in file:
        n.write(f"#{x}")
    
    new_file = open(f'{path_user_login}/get_hastag_user_login.txt', 'r', encoding="utf-8").read().split(' ')
    hastag = [x for x in new_file if '#' in x and x !="" and x != " " and x != "\n"]
    
    h = open(f'{path_user_login}/user_login_hastag.txt', 'a', encoding="utf-8")
    for x in hastag:
        if '\n' not in x and '#' in x:
            h.write(f'{x}\n')
    h.close()
    print("comparing with hastag")
    me = open(f'{path_user_login}/user_login_hastag.txt',encoding="utf8").read().splitlines()
    user = open(f'{path_data}/jus2_data.txt',encoding="utf8").read().splitlines()
    result=[]

    li=[]
    print("processing")
    users=[i.split(',') for i in user]
    for i in users:
        count=0
        h=open(f'{path_hastag}/{i[0]}_hastag.txt',encoding="utf8").read().splitlines()
        for x in me:
            if x in h:
                count+=1
                # print(".",end="")
        # print(".",end="")
        result.append(f"{i[0]},{i[1]},{count}")
        li.append(count)
    li.sort(reverse=True)
    rank=[]
    
    for a in range(10):
        rank.append(li[a])
        # print(".",end="")

    results=[x.split(',') for x in result]

    user_rank=[]
    for i in range(len(rank)):
        detail = {}
        for x in results:
            if int(x[2])==rank[i]:
                user_rank.append(x)
                print(x)
        # print(".",end="") 
    f.close()
    n.close()
    
    
    print("\n-----complete-----")
    return user_rank


