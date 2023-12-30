import random
from urllib.parse import urlparse
import requests

# ex key :   "X-RapidAPI-Key": "704d5c2221msh1b8993145546ac3p1ae21ajsn48ae9a8e7fae",


rapidkey = "7f1f9e377emshddad2d02e67b8e8p1ad475jsne0854cc579de"

# gets a user's followers
def get_followers(user):
    stans = []
    url = "https://soundcloud-scraper.p.rapidapi.com/v1/user/followers"
    querystring = {"user":f"https://soundcloud.com/{user}","limit":"200"}
    headers = {
        'X-RapidAPI-Key': rapidkey,
        "X-RapidAPI-Host": "soundcloud-scraper.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    for item in data['followers']['items']:
        stans.append(item)
    return stans

# gets a user's following
def get_following(user):
    stans = []
    url = "https://soundcloud-scraper.p.rapidapi.com/v1/user/followings"
    querystring = {"user":f"https://soundcloud.com/{user}","limit":"200"}
    headers = {
        "X-RapidAPI-Key": rapidkey,
        "X-RapidAPI-Host": "soundcloud-scraper.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    print(data)
    for item in data['followings']['items']:
        stans.append(item)
    return stans

# Get three random users from the list of followers
def get_random_users(listf):
    followers_list = listf

    # Ensure there are at least three followers
    if len(followers_list) >= 3:
        random_users = random.sample(followers_list, 3)
        return random_users
    else:
        print(f"Not enough followers")
        return []
    

def get_username_from_url(url):
    # Replace the common URL prefix and strip any spaces
    username = url.replace('https://soundcloud.com/', '').strip()

    return username



def FollowScheme(username):
    full_list = []
    myfollowers = get_followers(username)
    random_followers = get_random_users(myfollowers)
    user_count = 0
    for rnd in random_followers :
        full_list = get_followers(get_username_from_url(rnd['permalink']))
    print(get_username_from_url(full_list[0]))
    # while user_count < 20:
    #     get_followers


FollowScheme('777-leed')

        

    

