from view.authentification import AuthentificationMenu
from view.principal import MainView


def handle_authentication_choice(choice):

    from model.authentication import create_jwt, check_token

    if choice == "1":
        create_jwt()
    elif choice == "2":
        check_token()
    elif choice == "3":
        exit()

class AuthenticationControler(AuthentificationMenu):
    def __init__(self):
        AuthentificationMenu.main_authentification_menu()
        choice = MainView.choise()
        handle_authentication_choice(choice)














