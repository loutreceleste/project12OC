from view.principal import MainView
from view.support import SupportMenu


class SupportController(SupportMenu):
    def __init__(self, user):
        SupportMenu.support_menu()
        choice = MainView.choise()
        handle_support_choise(choice, user)

def handle_support_choise(choice, user):

    while True:
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 4:
                if choice == 1:
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
                    exit()
            else:
                print("Veuillez saisir un nombre entre 1 et 4!")
        else:
            print("Veuillez saisir un nombre entier!")

        SupportController(user)
        choice = MainView.choise()
