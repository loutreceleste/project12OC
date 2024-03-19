# This class is used to display the authentication menu
class AuthentificationMenu:
    # This method displays the main authentication menu
    @staticmethod
    def main_authentification_menu():
        print("\n-----MENU AUTHENTIFICATION-----")
        print("1) Générer un token d'authentification.")
        print("2) Me connecter avec mon token.")
        print("3) Quitter le programme.")

# This class is used to handle different views related to authentication
class AuthenticationViews:
    # This method handles the view to create a new authentication token
    @staticmethod
    def token_creation():
        print("\n-----CREATION D'UN TOKEN D'AUTHENTIFICATION-----")
        print("Attention, toute création de token engendrera un écrasement de "
              "l'ancien!")
        name_lastname = input("Nom et Prenom de votre compte: ")
        password = input("Votre mot de passe: ")
        return name_lastname, password

    # This method displays the created authentication token and some
    # instructions
    @staticmethod
    def token_print(encoded_jwt):
        print("Veuillez enregistrer votre token, assurez-vous de stocker vos "
              "jetons en toute sécurité et de ne "
              "jamais les divulguer à des tiers non autorisés.")
        print("Ce token expirera dans 2 jours à compter de maintenant.")
        print(encoded_jwt)

    # This method displays an error message when the authentication fails
    @staticmethod
    def error_authentication():
        print("Identifiant ou mot de passe incorrect. Vous allez être "
              "redirigée vers le Menu Authentifiaction.")

    # This method handles the view to enter the authentication token
    @staticmethod
    def token_cheking():
        print("\n-----CONNEXION AVEC VOTRE TOKEN-----")
        token = input("Veuillez insérer votre token: ")
        return token

    # This method displays a message when the authentication token has expired
    @staticmethod
    def expiration_date_token():
        print("Votre token a expiré. Veuillez générer un nouveau token.")

    # This method displays a message when the entered authentication token
    # is invalid
    @staticmethod
    def invalid_token():
        print("Token invalide. Veuillez vérifier votre token et réessayer.")
