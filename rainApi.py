from flask import * 
import json, time
from browsing import getFollow


app = Flask(__name__)

@app.route('/',methods=['GET'])
def home_page():
    data_set = {'Page':'Home','Message':'Great Success', 'TimeStamp':time.time()}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/user/',methods=['GET'])
def request_page():
    user_query = str(request.args.get('user'))
    followers_list = getFollow(user_query)
    follower_count = str(len(followers_list))
    data_set = {'Page':'Request','Message': f'You have {follower_count} followers', 'TimeStamp':time.time()}
    json_dump = json.dumps(data_set)
    return json_dump


if __name__ == '__main__':
    app.run(port=7777)
