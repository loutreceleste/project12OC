class ManagementMenu:
    def __init__(self, id, name, lastname, department, email):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.department = department
        self.email = email

class ManagementMenu:

    @staticmethod
    def management_menu(self):
        print(f"\n-----BONJOUR {self.lastname}-----")
        print("1) Menu collaborateurs.")
        print("2) Menu contrats.")
        print("3) Menu evenements.")
        print("4) Quitter la session.")

    @staticmethod
    def management_users_menu():
        print("\n-----MENU COLLABORATEURS-----")
        print("1) Créer un collaborateur.")
        print("2) Modifier un collaborateur.")
        print("3) Supprimer un collaborateur.")
        print("4) Afficher tout les collaborateurs.")
        print("5) Retour au Menu Gestion.")
        input("Votre choix: ")

    @staticmethod
    def management_contrats_menu():
        print("\n-----MENU CONTRATS-----")
        print("1) Créer un contrat.")
        print("2) Modifier un contrat.")
        print("3) Supprimer un contrat.")
        print("4) Afficher tout les contrats.")
        print("5) Retour au Menu Gestion.")
        input("Votre choix: ")

    @staticmethod
    def management_events_menu():
        print("\n-----MENU EVENEMENTS-----")
        print("1) Créer un évènement.")
        print("2) Modifier un évènement.")
        print("3) Supprimer un évènement.")
        print("4) Afficher tout les évènement.")
        print("5) Afficher tous les événements sans supports associés.")
        print("6) Retour au Menu Gestion.")
        input("Votre choix: ")

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