from admin_details import username,password
import requests
from termcolor import colored,cprint
from urllib import request

App_access_token = '5508711577.1063dec.210e3b7e96f14227b50f96e961f098d6'
Base_Url = 'https://api.instagram.com/v1/'


def self_info():
    request_url = Base_Url + "users/self/?access_token=" + App_access_token
    print("Get request url : ",request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print('Username : ',colored(user_info['data']['username'],'blue'))
            print("Name : ",colored(user_info['data']['full_name'],'blue'))
            print('No. of followers : ',colored(user_info['data']['counts']['followed_by'],'blue'))
            print('No. of people you are following : ',colored(user_info['data']['counts']['follows'],'blue'))
            print('No. of posts : ',colored(user_info['data']['counts']['media'],'blue'))
            print("")
            while (1):
                cprint("Enter choice :", 'yellow')
                print("1.Get followers list")
                print("2.Get following list")
                print("3.Get recent post")
                print("4.Recent media liked by me")
                print("5.Back to main menu")
                try:
                    choice = int(input(colored("Your choice : ", 'green')))
                except ValueError:
                    print(colored("Choose a valid option", 'red'))
                    get_user_info('mohit_s_jindal')
                if choice == 1:
                    list_of_users_this_user_is_followed_by('mohit_s_jindal')
                elif choice == 2:
                    list_of_users_this_user_follows('mohit_s_jindal')
                elif choice == 3:
                    get_own_post()
                elif choice == 4:
                    recent_media_liked_by_user()
                elif choice == 5:
                    menu()
                else:
                    print(colored("invalid option", 'red'))
                    menu()
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
            return None
    else:
        print(colored('Status code other than 200 received!', 'red'))
        menu()

def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        cprint("This user doesn't exist in your sandbox list",'red')
        menu()
    request_url = Base_Url + 'users/' + user_id + '?access_token=' + App_access_token
    print('GET request url :',request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print('Username : ', colored(user_info['data']['username'], 'blue'))
            print("Name : ", colored(user_info['data']['full_name'], 'blue'))
            print('No. of followers : ', colored(user_info['data']['counts']['followed_by'], 'blue'))
            print('No. of people user following : ', colored(user_info['data']['counts']['follows'], 'blue'))
            print('No. of posts : ', colored(user_info['data']['counts']['media'], 'blue'))
            print("")
            while(1):
                cprint("Enter choice :", 'yellow')
                print("1.Get followers list")
                print("2.Get following list")
                print("3.Get recent post")
                print("4.Back to main menu")
                try:
                    choice = int(input(colored("Your choice : ", 'green')))
                except ValueError:
                    print(colored("Choose a valid option", 'red'))
                    get_user_info(insta_username)
                if choice == 1:
                    list_of_users_this_user_is_followed_by(insta_username)
                elif choice == 2:
                    list_of_users_this_user_follows(insta_username)
                elif choice == 3:
                    get_user_post(insta_username)
                elif choice == 4:
                    menu()
                else:
                    print(colored("invalid option", 'red'))
                    menu()

        else:
            cprint('There is no data for this user!','green')
    else:
        print(colored('Status code other than 200 received!', 'red'))

def get_own_post():
    request_url = Base_Url + 'users/self/media/recent/?access_token=' + App_access_token
    print('GET request url :',request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            request.urlretrieve(image_url, image_name)
            cprint('Your image has been downloaded!','green')
        else:
            cprint("You doesn't have any post\n",'blue')
    else:
        print(colored('Status code other than 200 received!\n', 'red'))


def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        cprint("This user doesn't exist in your sandbox list", 'red')
        menu()
    request_url = Base_Url + 'users/' + user_id + '/media/recent/?access_token=' + App_access_token
    print('GET request url :',request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            request.urlretrieve(image_url,image_name)
            cprint("User's image has been downloaded!", 'green')
            print("")
            while(1):
                cprint("Enter your choice",'yellow')
                print("1.list of peoples likes this post")
                print("2.list of peoples comment on this post")
                print("3.Like this post")
                print("4.Comment on this post")
                print("5.Main menu")
                try:
                    choice = int(input(colored("Your choice : ", 'green')))
                except ValueError:
                    print(colored("Choose a valid option", 'red'))
                    get_user_post(insta_username)
                if choice == 1:
                    peoples_like_recent_post(insta_username)
                elif choice == 2:
                    peoples_comment_recent_post(insta_username)
                elif choice == 3:
                    like_a_post(insta_username)
                elif choice == 4:
                    post_a_comment(insta_username)
                elif choice == 5:
                    menu()
                else:
                    cprint("invalid choice")
                    menu()
        else:
            cprint("User doesn't have any post\n", 'blue')
    else:
        print(colored('Status code other than 200 received!\n', 'red'))


def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        cprint("This user doesn't exist in your sandbox list", 'red')
        menu()
    request_url = Base_Url + 'users/' + user_id + '/media/recent/?access_token=' + App_access_token
    print('GET request url :', request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            cprint("User doesn't have any post\n", 'blue')
    else:
        print(colored('Status code other than 200 received!\n', 'red'))

def peoples_like_recent_post(insta_username):
    post_id = get_post_id(insta_username)
    request_url = Base_Url + 'media/' + post_id + '/likes?access_token=' + App_access_token
    print('GET request url :', request_url)
    peoples = requests.get(request_url).json()

    if peoples['meta']['code'] == 200:
        if len(peoples['data']):
            position = 1
            cprint("Peoples like recent post",'cyan')
            for users in peoples['data']:
                print(position,colored(users['username'],'blue'))
                position += 1
        else:
            cprint("No one like this post",'blue')
    else:
        print(colored('Status code other than 200 received!\n', 'red'))


def recent_media_liked_by_user():
    request_url = Base_Url + 'users/self/media/liked?access_token=' + App_access_token
    print('GET request url :', request_url)
    media = requests.get(request_url).json()
    if media['meta']['code'] == 200:
        if len(media['data']):
            image_name = media['data'][0]['id'] + '.jpeg'
            image_url = media['data'][0]['images']['standard_resolution']['url']
            request.urlretrieve(image_url, image_name)
            cprint("User's image has been downloaded!", 'green')
            print("Post owner is",colored(media['data'][0]['user']['username'],'blue'))
            print("")
        else:
            cprint("You doesn't have any post\n",'blue')
    else:
        print(colored('Status code other than 200 received!\n', 'red'))





def peoples_comment_recent_post(insta_username):
    post_id = get_post_id(insta_username)
    request_url = Base_Url + 'media/' + post_id + '/comments?access_token=' + App_access_token
    print('GET request url :', request_url)
    peoples = requests.get(request_url).json()

    if peoples['meta']['code'] == 200:
        if len(peoples['data']):
            position = 1
            cprint("Peoples comment recent post",'cyan')
            for users in peoples['data']:
                print(position,colored(users['username'],'blue'))
                position += 1
        else:
            cprint("No one comment this post",'blue')
    else:
        print(colored('Status code other than 200 received!\n', 'red'))

def list_of_users_this_user_follows(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        cprint("This user doesn't exist in your sandbox list", 'red')
        menu()
    request_url = Base_Url + 'users/' + user_id + '/follows?access_token=' + App_access_token
    print('GET request url :', request_url)
    peoples = requests.get(request_url).json()
    if peoples['meta']['code'] == 200:
        if len(peoples['data']):
            position = 1
            cprint("Peoples this user follows",'cyan')
            for users in peoples['data']:
                print(position,colored(users['username'],'blue'))
                position += 1
        else:
            cprint("No one this user follows",'blue')
    else:
        print(colored('Status code other than 200 received!\n', 'red'))

def list_of_users_this_user_is_followed_by(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        cprint("This user doesn't exist in your sandbox list", 'red')
        menu()
    request_url = Base_Url + 'users/' + user_id + '/followed-by?access_token=' + App_access_token
    print('GET request url :', request_url)
    peoples = requests.get(request_url).json()
    if peoples['meta']['code'] == 200:
        if len(peoples['data']):
            position = 1
            cprint("This user is followed by", 'cyan')
            for users in peoples['data']:
                print(position, colored(users['username'], 'blue'))
                position += 1
        else:
            cprint("No one follow this user", 'blue')
    else:
        print(colored('Status code other than 200 received!\n', 'red'))



def like_a_post(insta_username):
    media_id = get_post_id(insta_username)
    request_url = Base_Url + 'media/' + media_id + '/likes'
    payload = {"access_token": App_access_token}
    print('POST request url :',request_url)
    like = requests.post(request_url, payload).json()
    if like['meta']['code'] == 200:
        cprint('Like successful!','green')
    else:
        cprint('Your like was unsuccessful. Try again!','red')

def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    text = raw_input(colored("Your comment: ",'cyan'))
    payload = {"access_token": App_access_token, "text" : text}
    request_url = Base_Url + 'media/' + media_id + '/comments'
    print('POST request url :',request_url)

    comment = requests.post(request_url, payload).json()

    if comment['meta']['code'] == 200:
        cprint("Successfully added a new comment!",'green')
    else:
        cprint("Unable to add comment. Try again!",'red')


def get_post_by_caption(insta_username):
    caption = input("Enter caption : ")
    user_id = get_user_id(insta_username)
    if user_id == None:
        cprint("This user doesn't exist in your sandbox list", 'red')
        menu()
    request_url = Base_Url + 'users/' + user_id + '/media/recent/?access_token=' + App_access_token
    print('GET request url :', request_url)
    user_media = requests.get(request_url).json()
    item = 1
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            for post in user_media['data']:
                if post['caption'] == caption:
                    image_name = str(item)+'.jpeg'
                    image_url = post['images']['standard_resolution']['url']
                    request.urlretrieve(image_url, image_name)
                    print(item,'post founded and saved')
                    item += 1
                else:
                    cprint("No post with this caption",'red')
        else:
            cprint("User doesn't have any post\n", 'blue')
    else:
        print(colored('Status code other than 200 received!\n', 'red'))




def Start_instaBot():
    user = input("Enter Username : ")
    pswrd = input("Enter Password : ")
    if user.upper() == username and pswrd == password:
        print(colored("Login Successful",'cyan'))
        print(colored("-----Wellcome to InstaBot-----\n",'blue'))
        menu()
    else:
        print(colored("Verification failed !\nPlease provide right Details\n",'red'))
        Start_instaBot()

def menu():
    while(1):
        cprint("Enter your choice\n", 'yellow')
        print("1.Get your own details")
        print("2.Get details of a user")
        print("3.Like a post(recently added)")
        print("4.Comment on a post(recently added)")
        print("5.Get post by perticular caption")
        print("6.Exit")
        try:
            choice = int(input(colored("Your choice : ",'green')))
        except ValueError:
            print(colored("Choose a valid option",'red'))
            menu()
        if choice == 1:
            self_info()
        elif choice == 2:
            insta_username = input("Enter username : ")
            get_user_info(insta_username)
        elif choice == 3:
            insta_username = input("Enter username : ")
            like_a_post(insta_username)
        elif choice == 4:
            insta_username = input("Enter username : ")
            post_a_comment(insta_username)
        elif choice == 5:
            insta_username = input("Enter username : ")
            get_post_by_caption(insta_username)
        elif choice == 6:
            exit()
        else:
            cprint("Invalid option",'red')

if __name__ == '__main__':
    Start_instaBot()