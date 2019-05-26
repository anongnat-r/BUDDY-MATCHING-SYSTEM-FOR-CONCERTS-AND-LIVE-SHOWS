from flask import Flask
from flask import render_template, jsonify,request,make_response
import json
import os

import key as key

from crawler_twitter_login import crawler
app = Flask(__name__)

@app.route('/')
# @app.route('/index')
def index():
    if len(os.listdir('./static/data/user_login') ) != 0:
        os.remove('./static/data/user_login/user_id.txt')
        os.remove("./static/data/user_login/user_login_hastag.txt")
        os.remove("./static/data/user_login/user_login.txt")
        os.remove('./static/data/user_login/get_hastag_user_login.txt')
    return render_template('index.html', config=key.config)

@app.route('/config')
def config():
    return jsonify(key.config)

@app.route('/key')
def getkey():
    return jsonify(key.key)

@app.route('/signin')
def signin():
    
    return render_template('signin.html',key=key.key, config=key.config)
@app.route('/signout')
def signout():
    return render_template('index.html')

@app.route('/jus2')
def jus2():
    
    user_rank=crawler()
    for i in range(len(user_rank)):
        print(f"rank#{i+1} : {user_rank[i][0]} score:{user_rank[i][2]}")
    print("got rank")
    return render_template('jus2.html',key=key.key, config=key.config,user_rank=user_rank)
    

@app.route('/uid',methods=[ 'POST'])
def uid():
    data = request.get_json()
    print(data)
    resp = make_response(json.dumps(data))
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    user=open('./static/data/user_login/user_id.txt','w',encoding='utf-8')
    user.write(data['key'])
    user.close()
     
if __name__ == '__main__':
   app.run(debug=True)
   