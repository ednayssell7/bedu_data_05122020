  
#tarea: usando conocimientos de python y request crear un bot para consultar los followers de un usuario de github
#despues descargar el avatar de cada follower 

import requests
# CONSTANTS
BASE_URL = 'https://api.github.com/'
# FUNCTIONS
def get_github_user(username):
    url = f'{BASE_URL}users/{username}'
    respose = requests.get(url)
    if respose.status_code == 200:
        return respose.json()
    return None

def download_github_user_avatar(avatar_url, username):
    response = requests.get(avatar_url)
    if response.status_code == 200:
        # download a file from internet
        response_content = response.content
        # open new folder 
        filename = f'tmp/{username}.png'
        with open(filename, 'wb') as image:
            image.write(response_content)
            return filename
    return None

def get_user_followers(username):
    url = f'{BASE_URL}users/{username}/followers'
    respose = requests.get(url)
    if respose.status_code == 200:
        return respose.json()
    return None
    
username = input('Give me a Github username:\t')
user = get_github_user(username)
user_followers = get_user_followers(username)
for follower in user_followers:
    download_github_user_avatar(follower['avatar_url'], follower['login'])
print('we have finished')