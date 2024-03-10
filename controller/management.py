from view.management import ManagementMenu
from view.principal import MainView


class ManagmentController(ManagementMenu):
    def __init__(self, user):
        ManagementMenu.management_menu()
        choice = MainView.choise()
        handle_management_choise(choice, user)

def handle_management_choise(choice, user):
    while True:
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 5:
                if choice == 1:
                    while True:
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 6:
                                if choice == 1:
                                elif choice == 2:
                                elif choice == 3:
                                elif choice == 4:
                                elif choice == 5:
                                elif choice == 6:
                            else:
                                print("Veuillez saisir un nombre entre 1 et 6!")
                        else:
                            print("Veuillez saisir un nombre entier!")
                if choice == 2:
                    while True:
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 3:
                                if choice == 1:
                                elif choice == 2:
                                elif choice == 3:
                            else:
                                print("Veuillez saisir un nombre entre 1 et 3!")
                        else:
                            print("Veuillez saisir un nombre entier!")
                if choice == 3:
                    while True:
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 5:
                                if choice == 1:
                                elif choice == 2:
                                elif choice == 3:
                                elif choice == 4:
                                elif choice == 5:
                            else:
                                print("Veuillez saisir un nombre entre 1 et 5!")
                        else:
                            print("Veuillez saisir un nombre entier!")
                if choice == 4:
                    while True:
                        if choice.isdigit():
                            choice = int(choice)
                            if 1 <= choice <= 5:
                                if choice == 1:
                                elif choice == 2:
                                elif choice == 3:
                                elif choice == 4:
                                elif choice == 5:
                            else:
                                print("Veuillez saisir un nombre entre 1 et 5!")
                        else:
                            print("Veuillez saisir un nombre entier!")

                if choice == 5:
                    exit()

            else:
                print("Veuillez saisir un nombre entre 1 et 5!")
        else:
            print("Veuillez saisir un nombre entier!")

        ManagmentController(user)
        choice = MainView.choise()