from getpass import getpass
import json


def json_update(x):
    j = json.dumps(x)
    with open('pass.json', 'w') as f:
        f.write(j)


def create_super(users):
    print("\nCreate a new Super User :")

    while True:
        userid = str(input("      New Userid : "))
        passwd = getpass("        Password :")
        passwdr = getpass("Reenter Password : ")

        if passwd == passwdr:
            if userid not in users["super"].keys() and users["manager"].keys() and users["local"].keys():
                users["super"][userid] = passwd
                json_update(users)
                print("\nUser created successfully ! ")
                break
            else:
                print("\nUserid already available try something else !")
                continue
        else:
            print("\nPassword mismatch!")


def create_manager(users):
    print("\nCreate a new Manager :")

    while True:
        userid = str(input("      New Userid : "))
        passwd = getpass("        Password :")
        passwdr = getpass("Reenter Password : ")

        if passwd == passwdr:
            if userid not in users["super"].keys() and users["manager"].keys() and users["local"].keys():
                users["manager"][userid] = [passwd]
                json_update(users)
                print("\nUser created successfully ! ")
                break
            else:
                print("\nUserid already available try something else !")
                continue
        else:
            print("\nPassword mismatch!")


def create_local(users):
    print("\nCreate a new Local User:")

    while True:
        userid = str(input("      New Userid : "))
        passwd = getpass("        Password :")
        passwdr = getpass("Reenter Password : ")

        if passwd == passwdr:
            if userid not in users["super"].keys() and users["manager"].keys() and users["local"].keys():
                users["local"][userid] = [passwd]
                json_update(users)
                print("\nUser created successfully ! ")
                break
            else:
                print("U\nserid already available try something else !")
                continue
        else:
            print("\nPassword mismatch!")


def create_alluser(users):
    while True:

        choice = str(input("\n (1)Super User || (2)Manager || (3)User || (4)Go Back : "))
        if choice == "1":
            create_super(users)
            break
        elif choice == "2":
            create_manager(users)
            break
        elif choice == "3":
            create_local(users)
            break
        elif choice == "4":
            break
        else:
            print("\nInvalid input !")


def delete_alluser(users):
    user_delete = str(input("\nEnter the userid to remove : "))
    x = ""
    y = 1
    z = 0
    for i in users.keys():
        for j in users[i].keys():
            if j == user_delete:
                x = i
                y = 1
                z = 1
                break
            else:
                y = 0
        if z == 1:
            break
    if y == 1:
        del users[x][user_delete]
        json_update(users)
        print("\nUser removed.")
    elif y == 0:
        print("\nUser not found !")


def delete_localuser(users):
    user_delete = str(input("\nEnter the userid to remove : "))

    y = 1
    for i in users["local"].keys():
        if i == user_delete:
            y = 1
            break
        else:
            y = 0
    if y == 1:
        del users["local"][user_delete]
        json_update(users)
        print("\nUser removed.")
    elif y == 0:
        print("\nUser not found !")


def show_user(users):
    super_users = ""
    managers = ""
    local_users = ""
    s = []
    m = []
    l = []
    for i in users.keys():
        for j in users[i].keys():
            if i == "super":
                s.append(j)
            elif i == "manager":
                m.append(j)
            elif i == "local":
                l.append(j)

    for i in s:
        super_users += " " + i + " "
    for i in m:
        managers += " " + i + " "
    for i in l:
        local_users += " " + i + " "
    print("\nSUPER USERS: ", super_users)
    print("   MANAGERS: ", managers)
    print("LOCAL USERS: ", local_users)
