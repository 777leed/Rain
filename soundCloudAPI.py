import requests



def stans(user):
    stans = []
    url = "https://soundcloud-scraper.p.rapidapi.com/v1/user/followers"
    querystring = {"user":f"https://soundcloud.com/{user}","limit":"200"}
    headers = {
        "X-RapidAPI-Key": "704d5c2221msh1b8993145546ac3p1ae21ajsn48ae9a8e7fae",
        "X-RapidAPI-Host": "soundcloud-scraper.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    print(data)
    for item in data['followers']['items']:
        stans.append(item)
    return stans


def staned(user):
    stans = []
    url = "https://soundcloud-scraper.p.rapidapi.com/v1/user/followings"
    querystring = {"user":f"https://soundcloud.com/{user}","limit":"200"}
    headers = {
        "X-RapidAPI-Key": "704d5c2221msh1b8993145546ac3p1ae21ajsn48ae9a8e7fae",
        "X-RapidAPI-Host": "soundcloud-scraper.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    for item in data['followings']['items']:
        stans.append(item)
    return stans
