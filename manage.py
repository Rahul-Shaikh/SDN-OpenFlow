import user_management
import local


class Manager(local.Local):
    def user_mng(self,users):
        while True:
            choice = str(input("\n(1) Show Users || (2)Create Users || (3)Remove Users(Local only) || (4) Go Back : "))
            if choice == "1":
                user_management.show_user(users)

            elif choice == "2":
                user_management.create_local(users)

            elif choice == "3":
                user_management.delete_localuser(users)
            elif choice == "4":
                break
            else:
                print("Invalid Input !")


def driver_manager(users,name):
    while True:
        choice = str(input("{}>> ".format(name.lower())))
        if choice == "user manage":
            Manager().user_mng(users)
        elif choice == "quit":
            break
        else:
            print("Invalid input !")
    return choice
