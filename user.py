# user.py
from pymongo import errors as err
from post import *
from follow import *
from newsfeed import *
from wall import *

def password_chk():
    while(True):
        pw1 = input('\ninput password : ')
        pw2 = input('input password again : ')

        if not pw1:
            print('please, fill in')
        elif pw1 != pw2:
            print('wrong password, try again')
        else:
            return pw1


def verify(type, user_input):
    while(True):
        is_chk = input('your {} is {}, right? answer y or n : '.format(type, user_input)).lower()
        if is_chk == 'y':
            return True
        elif is_chk == 'n':
            return False
        else:
            print('type only y or n')



def input_func(type):
    while(True):
        user_input = input('\ninput {} : '.format(type))
        if user_input:
            if verify(type, user_input):
                return user_input
        else:
            print('please, fill in')


def signup(db):

    user_c = db.user
    print('\n----- signup -----')

    id = input_func('ID')

    pw = password_chk()

    name = input_func('Name')

    try:
        user_c.insert({'_id':id, 'pw':pw, 'name':name, 'status':None, 'follower':[], 'followings':[]})
        signin(db)
        # user_c.update({'_id': id}, {'$set': {'pw': pw1, 'name': name}})

    except err.DuplicateKeyError:
        print('duplicated ID, retry!')
        signup(db)


def signin(db):

    print('\n---- login -----')
    user_id = input("please input your id : ")
    user_pw = input("please input your password : ")

    if list(db.user.find({'_id':user_id,'pw':user_pw})): #and list(db.user.find({'pw':user_pw})):
        userpage(db, user_id)
    else :
        print("please Check your id or pw")
        signin(db)



def mystatus(db, user):
    '''
    print user profile, # followers, and # followings
    '''
    #-------------------------변수공간-----------------------------------------------

    user_name = db.user.find_one({"_id":user})["name"]
    user_status = db.user.find_one({"_id": user})["status"]
    user_follower = db.user.find_one({"_id":user})["follower"]
    user_following = db.user.find_one({"_id":user})["followings"]

    #------------------------------------------------------------------------------

    print("\nUser_name : ", user_name)
    print("User_status : ", user_status)
    if user_follower:
        print("Your follower list : ", user_follower)
    else: print("Your follower list is empty")

    if user_following:
        print("Your following list : ", user_following)
    else: print("Your following list is empty")

    print("-"*80)
    print(" 1 : change my status \n"
          " 2 : change password \n"
          " 3 : go to userpage \n"
          " 4 : quit \n"
          )

    do = int(input("please input number want to do: "))

    switcher = {1 : change_status,
                2 : change_pw,
                3 : userpage,
                4 : quit}

    role_menu = switcher.get(do)
    role_menu(db,user)


def change_status(db, user):
    print(" 1 : change my status to 'good' \n"
          " 2 : change my status to 'soso' \n"
          " 3 : change my status to 'bad' \n"
          )
    do = int(input("please input number want to do: "))
    switcher = {1 : 'good',
                2 : 'soso',
                3 : 'bad'}
    user_status = switcher.get(do)
    db.user.update({'_id': user}, {'$set': {'status': user_status}})
    print('status succesfully updated')
    mystatus(db, user)


def change_pw(db, user):
    pw = input('type current password : ')
    if pw == db.user.find_one({'_id': user})['pw']:
        print(('\ntype new password'))
        new_pw = password_chk()
        db.user.update({'_id': user}, {'$set': {'pw': new_pw}})
        print('\npassword succesfully updated')
    else:
        print('\nwrong password')
    mystatus(db, user)


def userpage(db, user):
    '''
    user page
    '''
    while True:
        print()
        print("-"*80)
        print(" 1 : go to Post_Interface \n"
              " 2 : go to my status \n"
              " 3 : go to follow \n"
              " 4 : go to unfollow \n"
              " 5 : go to newsfedd \n"
              " 6 : go to wall \n"
              " 7 : quit \n"
              )

        do = int(input("please input number want to do: "))

        switcher = {1 : postInterface,
                    2 : mystatus,
                    3 : follow,
                    4 : unfollow,
                    5 : getPosts,
                    6 : wall,
                    7 : quit
                    }

        role_menu = switcher.get(do)

        role_menu(db,user)


def quit(db,user):
    sys.exit()