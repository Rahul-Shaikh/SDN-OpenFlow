#!/usr/bin/python3
from os import system
from getpass import getpass
from datetime import datetime, date
import json
import super
import manage
import local


_ = system("clear")


def logout(x):
    logout_choice = x
    if logout_choice == "quit":
        quit()


while True:
    users = json.load(open("pass.json"))
    user_name = str(input("  Userid : "))
    password = getpass("Password :")
    if user_name in users["super"].keys():
        if users["super"][user_name] == password:
            print("\n   Welcome : {}+ (Superuser) ".format(user_name) + str(date.today()) + " " + str(datetime.now())+"\n")
            x=super.driver_super(users,user_name)
            logout(x)
    elif user_name in users["manager"].keys():
        if users["manager"][user_name] == password:
            print("\n   Welcome : {} + (Manager) ".format(user_name) + str(date.today()) + " " + str(datetime.now())+"\n")
            x=manage.driver_manager(users,user_name)
            logout(x)
    elif user_name in users["local"].keys():
        if users["local"][user_name] == password:
            print("\n   Welcome : {}+ (Local User) ".format(user_name) + str(date.today()) + " " + str(datetime.now())+"\n")
            x=local.driver_local(users,user_name)
            logout(x)
    else:
        _ = system("clear")
        print("Wrong Username or Password")
