import requests
from termcolor import colored
App_access_token = '5508711577.1063dec.210e3b7e96f14227b50f96e961f098d6'
Base_Url = 'https://api.instagram.com/v1/'


def self_info():
    request_url = Base_Url + "users/self/?access_token=" + App_access_token
    print("Get request url : ",request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print('Username : ',colored(user_info['data']['username'],'blue'))
            print('No. of followers : ',colored(user_info['data']['counts']['followed_by'],'blue'))
            print('No. of people you are following : ',colored(user_info['data']['counts']['follows'],'blue'))
            print('No. of posts : ',colored(user_info['data']['counts']['media'],'blue'))
        else:
            print(colored('User does not exist!','red'))
    else:
        print(colored('Status code other than 200 received!','red'))

def get_user_id(insta_username):
    request_url = Base_Url + 'users/search?q=' + insta_username + '&access_token=' + App_access_token
    print('GET request url : ',request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return colored("This user doesn't exist in your sandbox list",'red')
    else:
        print(colored('Status code other than 200 received!', 'blue'))
        exit()


self_info()
username = input("Enter username ")
print(get_user_id(username))