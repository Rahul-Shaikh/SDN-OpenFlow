#!/usr/bin/python3
from os import system
from getpass import getpass
from datetime import datetime, date
import json
import super
import manage
import local
import hashlib


_ = system("clear")


def logout(lo):
    logout_choice = lo
    if logout_choice == "quit":
        quit()


while True:
    users = json.load(open("pass.json"))
    user_name = str(input("  Userid : "))
    password = (getpass("Password :")).encode("utf-8")

    if user_name in users.keys():
        x = eval(users[user_name][2])
        y = hashlib.sha256(password + x).hexdigest()

        if users[user_name][1] == str(y):
            if users[user_name][0]=="super":
                print("\n   Welcome : {} (Superuser) ".format(user_name) + str(date.today()) + " " + str(datetime.now()) + "\n")
                x=super.driver_super(users,user_name)
                logout(x)

            elif users[user_name][0]=="manager":
                print("\n   Welcome : {}  (Manager) ".format(user_name) + str(date.today()) + " " + str(datetime.now())+"\n")
                x=manage.driver_manager(users,user_name)
                logout(x)

            elif users[user_name][0]=="local":
                print("\n   Welcome : {} (Local User) ".format(user_name) + str(date.today()) + " " + str(datetime.now())+"\n")
                x=local.driver_local(users,user_name)
                logout(x)

        else:
            _ = system("clear")
            print("Wrong Username or Password")

    else:

        _ = system("clear")
        print("Wrong Username or Password")
