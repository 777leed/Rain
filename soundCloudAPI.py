import random
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
def get_random_users(x, followers_list):
    # Ensure there are followers in the list
    if len(followers_list) > 0:
        if x <= len(followers_list):
            random_users = random.sample(followers_list, x)
        else:
            print(f"Requested more users than available. Returning all {len(followers_list)} followers.")
            random_users = followers_list
        return random_users
    else:
        print("No followers available.")
        return []
    



def get_username_from_url(url):
    # Replace the common URL prefix and strip any spaces
    username = url.replace('https://soundcloud.com/', '').strip()

    return username


### random returns usernames
def FollowSchemeUser(username):
    #list to store random users to follow
    full_list = []
    user_list = []
    #getting followers from my profile
    print('getting your followers...')
    myfollowers = get_followers(username)
    # getting random users from my list of followers
    print('choosing 3 of your followers at random...')
    random_followers = get_random_users(3, myfollowers)
    for rnd in random_followers :
        user_list.append(get_username_from_url(rnd['permalink']))
    print('Loading Followers chosen...')    
    print(user_list)
    usr_cnt = 0  
    print('Loading Followers of the selected users...')  
    for usr in user_list :
        usr_cnt = usr_cnt + 1
        print('Loading Followers of user ' + str(usr_cnt) + '...')
        user_followers = get_followers(usr)
        print('Loading 8 Random Followers of user ' +str(usr_cnt)+ '...')    
        random_followers_users = get_random_users(8, user_followers)
        for rnd in random_followers_users :
            full_list.append(get_username_from_url(rnd['permalink']))
        print('Clearing list of user ' +str(usr_cnt)+ '...')    
        random_followers_users.clear()    
    print(full_list)  


### random returns lists with info

def FollowSchemeList(username):
    #list to store random users to follow
    full_list = []
    user_list = []
    #getting followers from my profile
    print('getting your followers...')
    myfollowers = get_followers(username)
    # getting random users from my list of followers
    print('choosing 3 of your followers at random...')
    random_followers = get_random_users(3, myfollowers)
    for rnd in random_followers :
        user_list.append(get_username_from_url(rnd['permalink']))
    print('Loading Followers chosen...')    
    print(user_list)
    usr_cnt = 0  
    print('Loading Followers of the selected users...')  
    for usr in user_list :
        usr_cnt = usr_cnt + 1
        print('Loading Followers of user ' + str(usr_cnt) + '...')
        user_followers = get_followers(usr)
        print('Loading 8 Random Followers of user ' +str(usr_cnt)+ '...')    
        random_followers_users = get_random_users(8, user_followers)
        for rnd in random_followers_users :
            full_list.append(rnd)
        print('Clearing list of user ' +str(usr_cnt)+ '...')    
        random_followers_users.clear()    
    return full_list         



