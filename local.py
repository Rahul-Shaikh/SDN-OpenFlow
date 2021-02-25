import user_management


class Local:

    def user_mng(self, users):
        while True:
            choice = str(input("\n(1)Show Users || (2)Create Users || (3)Go Back : "))
            if choice == "1":
                user_management.show_user(users)

            elif choice == "2":
                user_management.create_local(users)

            elif choice == "3":
                break
            else:
                print("Invalid Input !")


def driver_local(users,name):
    while True:
        choice = str(input("{}>> ".format(name.lower())))
        if choice == "user manage":
            Local().user_mng(users)
        elif choice == "quit":
            break
        else:
            print("Invalid input !")
    return choice
