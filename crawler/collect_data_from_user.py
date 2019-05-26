from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import tweepy


with open('./js/key.json', 'r') as f:
    distros_dict = json.load(f)
key=[]
for distro in distros_dict:
    key.append(distros_dict[distro])

consumer_key = key[0]
consumer_secret = key[1]
access_token = key[2]
access_secret = key[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


number_of_tweets = 10**6
user_name = open('./data/user_name.txt').read().splitlines()
visited= open('./data/visited_user.txt').read().splitlines()
for user in range(len(visited),len(user_name)):
    print(f"visiting : {user_name[user]}")
    name = "@"+user_name[user]
    count = 0
    f = open(f"./data/user_data/{user_name[user]}.txt", 'a', encoding='utf-8')
    for status in tweepy.Cursor(api.user_timeline, screen_name=name, tweet_mode="extended").items():
        if count >= number_of_tweets:
            break
        count += 1
        f.write(status.full_text)
    visit=open('./data/visited_user.txt','a',encoding='utf-8')
    visit.write(f"\n{user_name[user]}")
    print(f"got user: {user_name[user]}")
    visited= open('./data/visited_user.txt').read().splitlines()
    print(f"total: {len(visited)}")
    file=open(f'./data/user_data/{user_name[user]}.txt','r',encoding='utf-8').read().split('#')
    n=open(f'./data/user_data/hastag/get_hastag_{user_name[user]}.txt','a',encoding="utf-8")
    for x in file:
        n.write(f"#{x}")
    new_file=open(f'./data/user_data/hastag/get_hastag_{user_name[user]}.txt','r',encoding="utf-8").read().split(' ')
    hastag = [x for x in new_file if '#' in x and x!="" and x!=" " and x!="\n"]
    h=open(f'./data/user_data/hastag/{user_name[user]}_hastag.txt','a',encoding="utf-8")
    for x in hastag:
        if '\n' not in x and '#' in x:
            h.write(f'{x}\n')