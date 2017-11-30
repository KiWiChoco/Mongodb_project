# main.py
from user import *
from pymongo import MongoClient
import pymongo

def mainpage(db):
    '''
    call signup() or signin()
    '''

    print("Welcome")
    print(" 1 : signup \n"
          " 2 : singin \n"
          )

    do = int(input("please input number want to do : "))

    switcher = {1 : signup,
                2 : signin
                }

    role_menu = switcher.get(do)
    role_menu(db)

if __name__ == "__main__":
    '''
    call mainpage()
    '''
    client = MongoClient()
    db = client.project
    mainpage(db)
