from getpass import getpass
import json
import crypt
import hashlib


def json_update(x):
    j = json.dumps(x)
    with open('pass.json', 'w') as f:
        f.write(j)


def create_super(users):
    print("\nCreate a new Super User :")

    while True:
        userid = str(input("      New Userid : "))
        if userid in users.keys():
            print("\nUserid already available try something else !")
            continue
        else:
            passwd = getpass("        Password :")
            passwdr = getpass("Reenter Password : ")

            if passwd == passwdr:

                x = crypt.mksalt(crypt.METHOD_SHA256).encode('utf-8')
                y = hashlib.sha256(passwd.encode("utf-8") + x).hexdigest()
                users[userid] = ["super", str(y), str(x)]
                json_update(users)
                print("\nUser created successfully ! ")
                break

            else:
                print("\nPassword mismatch!")


def create_manager(users):
    print("\nCreate a new Manager :")

    while True:
        userid = str(input("      New Userid : "))
        if userid in users.keys():
            print("\nUserid already available try something else !")
            continue
        else:
            passwd = getpass("        Password :")
            passwdr = getpass("Reenter Password : ")

            if passwd == passwdr:

                x = crypt.mksalt(crypt.METHOD_SHA256).encode('utf-8')
                y = hashlib.sha256(passwd.encode("utf-8") + x).hexdigest()
                users[userid] = ["manager", str(y), str(x)]
                json_update(users)
                print("\nUser created successfully ! ")
                break

            else:
                print("\nPassword mismatch!")


def create_local(users):
    print("\nCreate a new Local User:")

    while True:
        userid = str(input("      New Userid : "))
        if userid in users.keys():
            print("\nUserid already available try something else !")
            continue
        else:
            passwd = getpass("        Password :")
            passwdr = getpass("Reenter Password : ")

            if passwd == passwdr:

                x = crypt.mksalt(crypt.METHOD_SHA256).encode('utf-8')
                y = hashlib.sha256(passwd.encode("utf-8") + x).hexdigest()
                users[userid] = ["local", str(y), str(x)]
                json_update(users)
                print("\nUser created successfully ! ")
                break

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
    y = 1
    for i in users.keys():
        if i == user_delete:
            y = 1
            break
        else:
            y = 0

    if y == 1 and len(users) > 1:
        del users[user_delete]
        json_update(users)
        print("\nUser removed.")
    elif y == 0:
        print("\nUser not found !")
    else:
        print("\nCan't remove the only user\n")


def delete_localuser(users):
    user_delete = str(input("\nEnter the userid to remove : "))

    y = 1
    for i in users.keys():
        if i == user_delete and users[i][0] == "local":
            y = 1
            break
        else:
            y = 0
    if y == 1:
        del users[user_delete]
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

        if users[i][0] == "super":
            s.append(i)
        elif users[i][0] == "manager":
            m.append(i)
        elif users[i][0] == "local":
            l.append(i)

    for i in s:
        super_users += " " + i + " "
    for i in m:
        managers += " " + i + " "
    for i in l:
        local_users += " " + i + " "
    print("\nSUPER USERS: ", super_users)
    print("   MANAGERS: ", managers)
    print("LOCAL USERS: ", local_users)
