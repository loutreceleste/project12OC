from model.management import User
from database import session

class MainMenu:
    @staticmethod
    def registration_informations():
        print("\n-----VEUILLEZ VOUS CONNECTER-----")
        lastname = input("Nom: ")
        password = input("Mot de passe: ")
        return lastname, password

    @staticmethod
    def input_error():
        print("Erreur de saisie!")

    @staticmethod
    def show_all_users():
        print("\n---ALL USERS---")
        users = session.query(User).all()
        for user in users:
            print(f"ID: {user.user_id}, Nom: {user.user_lastname}, Departement: {user.user_departement},"
                  f"Nom: {user.user_lastname}, Email: {user.user_email}")
