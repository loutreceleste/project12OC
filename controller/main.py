import jwt
from sqlalchemy.orm import declarative_base

from controller.management import ManagementController
from controller.support import SupportController
from controller.sales import SalesController

from view.authentification import AuthentificationMenu, AuthenticationViews
from view.principal import MainView

from model.authentication import create_jwt, check_token, check_user, decode_token

from sentry_config import initialize_sentry


Base = declarative_base()

initialize_sentry()

class MainController(AuthentificationMenu):
    def __init__(self):
        AuthentificationMenu.main_authentification_menu()
        choice = MainView.choise()
        handle_authentication_choice(choice)

def handle_authentication_choice(choice):
    while True:
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 3:
                if choice == 1:
                    name_lastname, password = AuthenticationViews.token_creation()
                    user = check_user(name_lastname, password)
                    if user:
                        encoded_jwt = create_jwt(user)
                        AuthenticationViews.token_print(encoded_jwt)
                    else:
                        AuthenticationViews.error_authentication()
                elif choice == 2:
                    token = AuthenticationViews.token_cheking()
                    user = check_token(token)
                    if user:
                        try:
                            decoded_jwt = decode_token(token, user)
                            if decoded_jwt:
                                MainView.message_connection_token()
                                if user.department == 'COM':
                                    SalesController(user)
                                elif user.department == 'GES':
                                    ManagementController(user)
                                elif user.department == 'SUP':
                                    SupportController(user)
                                else:
                                    MainView.message_no_department()
                            else:
                                AuthenticationViews.invalid_token()
                        except jwt.ExpiredSignatureError:
                            AuthenticationViews.expiration_date_token()
                        except jwt.InvalidTokenError:
                            AuthenticationViews.invalid_token()
                    else:
                        AuthenticationViews.invalid_token()
                elif choice == 3:
                    exit()
            else:
                print("Veuillez saisir un nombre entre 1 et 3!")
        else:
            MainView.message_no_whole_number()

        MainController()
        choice = MainView.choise()

if __name__ == "__main__":
    MainController()
