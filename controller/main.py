from view.authentification import AuthentificationMenu, AuthenticationViews
from view.principal import MainView
from model.authentication import create_jwt, check_token, check_user, decode_token

from controller.sales import SalesController


class MainController(AuthentificationMenu):
    def __init__(self):
        AuthentificationMenu.main_authentification_menu()
        choice = MainView.choise()
        handle_authentication_choice(choice)

def handle_authentication_choice(choice):

    if choice == "1":
        name_lastname, password = AuthenticationViews.token_creation()
        user = check_user(name_lastname, password)
        if user:
            encoded_jwt = create_jwt(user)
            AuthenticationViews.token_print(encoded_jwt)
            MainController()
        else:
            AuthenticationViews.error_authentication()
            MainController()
    elif choice == "2":
        token = AuthenticationViews.token_cheking()
        user = check_token(token)
        if user:
                decoded_jwt = decode_token(token, user)
                if decoded_jwt:
                    print("Connexion réussie avec votre token.")
                    if user.department == 'COM':
                        SalesController(user)
                    elif user.department == 'GES':
                        print('GES')
                    elif user.department == 'SUP':
                        print('SUP')
                    else:
                        print("Impossible de récupérer le département de l'utilisateur.")
                else:
                    AuthenticationViews.invalid_token()
                    MainController()
        else:
            AuthenticationViews.invalid_token()
            MainController()
    elif choice == "3":
        exit()

if __name__ == "__main__":
    MainController()
