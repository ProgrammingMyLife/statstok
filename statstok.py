import requests
from bs4 import BeautifulSoup



def get_followers(username):
    URL = f'https://www.tiktok.com/@{username}?lang=en'
    page = requests.get(URL, headers={"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"})

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find()

    stats = results.find_all('div', class_='share-layout-content jsx-2997938848')
    followercount = None
    for items in stats:
        followercount = items.find("strong", title="Followers")

    try :
        return followercount.text

    except AttributeError :
        return "Error occured! That user does not exist"

def get_likes(username):
    URL = f'https://www.tiktok.com/@{username}?lang=en'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find()

    stats = results.find_all('div', class_='share-layout-content jsx-2997938848')
    likecount = None
    for items in stats:
        likecount = items.find("strong", title="Likes")
    
    try :
        return likecount.text
    
    except AttributeError:
        return "Error occured! That user does not exist"
