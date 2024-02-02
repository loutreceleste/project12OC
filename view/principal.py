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
    def choise():
        return input("Votre choix: ")

    @staticmethod
    def delete():
        return input("Effacer")

    @staticmethod
    def change():
        return input("Modifier")