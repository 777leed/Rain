from flask import Flask, render_template
from soundCloudAPI import stans, staned



#☁️
app = Flask(__name__)

#☁️
def get_users_not_following_back(username):
    
    followers = stans(username)
    following = staned(username)

    followers_usernames = [follower['id'] for follower in followers]

    not_following_back_users = [followed for followed in following if followed['id'] not in followers_usernames]

    return not_following_back_users

def format_follow_count(count):
    if count < 1000:
        return str(count)
    elif count < 1000000:
        return str(count // 1000) + 'K'
    else:
        return str(count // 1000000) + 'M'
#☁️
@app.route('/stans/<username>')
def hello(username):
    imposters = get_users_not_following_back(username)
    cards = []

    for follower in imposters:
        cards.append(
            {
                'profile_url': follower['permalink'],
                'image_url': follower['avatarUrl'],
                'title': follower['name'],
                'subtitle': format_follow_count(follower['followerCount']) + ' followers',
                'subtitle2': format_follow_count(follower['followingCount']) + ' following'
            }
        )
    
    return render_template('home.html', cards=cards)

#☁️
if __name__ == '__main__':
    app.run(port=7777)
