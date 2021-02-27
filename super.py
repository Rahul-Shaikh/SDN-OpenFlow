import manage
import user_management
from os import system


class Super(manage.Manager):
    def user_mng(self, users):

        while True:
            choice = str(input("\n(1)Show Users || (2)Create Users || (3)Remove users  || (4)Go Back : "))
            if choice == "1":
                user_management.show_user(users)
            elif choice == "2":
                user_management.create_alluser(users)

            elif choice == "3":
                user_management.delete_alluser(users)

            elif choice == "4":
                break
            else:
                print("Invalid Input !")


def driver_super(users, name):
    while True:
        choice = str(input("{}>> ".format(name.lower())))
        if choice == "usermanage":
            Super().user_mng(users)
        elif choice == "ls":
            _ = system("ls")
        elif choice == "quit":
            break
        else:
            print("Invalid input !")
    return choice
