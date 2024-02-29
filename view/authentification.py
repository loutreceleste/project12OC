class AuthentificationMenu:

    @staticmethod
    def main_authentification_menu():
        print(f"\n-----MENU AUTHENTIFICATION-----")
        print("1) Générer un token d'authentification.")
        print("2) Me connecter avec mon token.")
        print("3) Quitter le programme.")

class AuthenticationViews:

    @staticmethod
    def token_creation():
        print("\n-----CREATION D'UN TOKEN D'AUTHENTIFICATION-----")
        print("Attention, toute création de token engendrera un écrasement de l'ancien!")
        name_lastname = input("Votre Nom et Prenom de votre compte: ")
        password = input("Votre mot de passe: ")
        return name_lastname, password

    @staticmethod
    def token_print(encoded_jwt):
        print("Veuillez enregistrer votre token, assurez-vous de stocker vos jetons en toute sécurité et de ne "
              "jamais les divulguer à des tiers non autorisés.")
        print("Ce token expirera dans 2 jours à compter de maintenant.")
        print(encoded_jwt)

    @staticmethod
    def error_authentication():
        print("Identifiant ou mot de passe incorrect. Vous allez être redirigée vers le Menu Authentifiaction.")

    @staticmethod
    def token_cheking():
        print("\n-----CONNEXION AVEC VOTRE TOKEN-----")
        token = input("Veuillez insérer votre token: ")
        return token

    @staticmethod
    def expiration_date_token():
        print("Votre token a expiré. Veuillez générer un nouveau token.")

    @staticmethod
    def invalid_token():
        print("Token invalide. Veuillez vérifier votre token et réessayer.")