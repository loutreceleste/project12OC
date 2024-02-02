from principal import MainMenu

class ManagementMenu:

    def __init__(self, id, name, lastname, department):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.department = department

    @staticmethod
    def new_collaborator_informations():
        print("\n-----NOUVEAU COLLABORATEUR-----")
        name = input("Prénom: ")
        lastname = input("Nom: ")
        print("\n-----LES DEPARTEMENTS A RESEIGNER:-----")
        print("-----COM: COMMERCIAL-----")
        print("-----GES: GESTION-----")
        print("-----SUP: SUPPORT-----")
        department = input("Departement: ")
        password = input("Mot de passe: ")
        return name, lastname, department, password

    @staticmethod
    def management_menu(managementmenu):
        print("\n-----BONJOUR {self.lastname}-----")
        print("1) Menu comptes utilisateurs.")
        print("2) Menu contrats.")
        print("3) Menu evenements.")
        print("3) Quitter la session.")

    @staticmethod
    def management_users_menu():
        print("\n-----MENU COLLABORATEURS-----")
        print("1) Créer un collaborateur.")
        print("2) Afficher tout les collaborateurs.")
        print("3) Retour au Menu Gestion.")

    @staticmethod
    def management_contrats_menu():
        print("\n-----MENU CONTRATS-----")
        print("1) Créer un contrat.")
        print("2) Afficher tout les contrat.")
        print("3) Retour au Menu Gestion.")

    @staticmethod
    def management_events_menu():
        print("\n-----MENU EVENEMENTS-----")
        print("1) Afficher les évènements sans support associé.")
        print("2) Afficher tout les évènements.")
        print("3) Retour au Menu Gestion.")

