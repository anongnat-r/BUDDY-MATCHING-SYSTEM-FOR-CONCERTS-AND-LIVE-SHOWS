# -*- coding: UTF-8 -*-
import codecs
import io
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import sys

with open('./js/key.json', 'r') as f:
    distros_dict = json.load(f)
key=[]
for distro in distros_dict:
    key.append(distros_dict[distro])

consumer_key = key[0]
consumer_secret = key[1]
access_token = key[2]
access_secret = key[3]
thailand_th = open('./data/thailand_th.txt','r',encoding='utf-8').read().splitlines()
thailand_en = open('./data/thailand_en.txt').read().splitlines()

thailand=thailand_en+thailand_th
IsTH = False
count=0
class MyListener(StreamListener):

    def on_data(self, data):
        try:
            
            with open('./data/nadech_data.json', 'a') as f:
                
                f.write(data)
                dat = json.loads(data)
                file = open('./data/nadech_data.txt','a')
                user_name= dat['user']['screen_name']
                location=dat['user']['location']
               
                
                image=dat['user']['profile_image_url']
                lang=dat['user']['lang']
                
                b=location.split(',')
                print(f"จังหวัด หรือ ประเทศ: {b}")
                th = ""
                if len(b)>1:
                    for x in b[-1]:
                        if x!=" " and x!="":
                            th+=x
                else:
                    for x in b:
                        if x!=" " and x!="":
                            th+=x


                
                # print(f"lang: {lang.upper()}")
                # print(f"th: {th}")
                # print(f"th: {th.upper()}")
                
                if (lang.upper()=='TH') or (th in thailand) or (th.upper() in thailand) :
                    print('---- get it ----')
                    file.write(f"{user_name},{image}\n")
                if count==250:
                    file.close()
                    sys.exit()   
                
                # print(f">> {dat['created_at']} {dat['text']}\n")
        except BaseException as e:
            print(f"--> Error on_data: {str(e)}")
            pass
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    twitter_stream = Stream(auth, MyListener())

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    twitter_stream.filter(track=['ณเดชณ์', '#ณเดชณ์','nadech','#nadech','TheRealNadechConcert','ณเดช','#ณเดช'])
    