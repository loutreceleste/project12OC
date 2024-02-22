class MenuAuthentification:

    @staticmethod
    def main_authentification_menu():
        print(f"\n-----MENU AUTHENTIFICATION-----")
        print("1) Générer un token d'authentification.")
        print("2) Me connecter avec mon token.")
        print("3) Quitter le programme.")

    @staticmethod
    def token_menu():
        print(f"\n-----MENU TOKEN-----")
        print("1) Menu collaborateurs.")
        print("1) Menu clients.")
        print("2) Menu contrats.")
        print("3) Menu evenements.")
        print("4) Quitter la session.")
        return input("Votre choix: ")

    @staticmethod
    def registration_informations():
        print("\n-----VEUILLEZ VOUS CONNECTER-----")
        name_lastname = input("Nom et prénom: ")
        password = input("Mot de passe: ")
        return name_lastname, password