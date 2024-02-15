from database import session
from model.management import Event, User


class ManagementMenu:
    @staticmethod
    def management_menu(self):
        print(f"\n-----BONJOUR {self.lastname}-----")
        print("1) Menu collaborateurs.")
        print("1) Menu clients.")
        print("2) Menu contrats.")
        print("3) Menu evenements.")
        print("4) Quitter la session.")
        return input("Votre choix: ")

    @staticmethod
    def management_users_menu():
        print("\n-----MENU COLLABORATEURS-----")
        print("1) Créer un collaborateur.")
        print("2) Modifier un collaborateur.")
        print("3) Supprimer un collaborateur.")
        print("3) Rechercher un collaborateur.")
        print("4) Afficher tout les collaborateurs.")
        print("5) Retour au Menu Gestion.")
        return input("Votre choix: ")

    @staticmethod
    def id_change_user():
        print("Quel collaborateur souhaitez-vous modifier?")
        return input("ID du collaborateur: ")

    @staticmethod
    def id_delete_user():
        print("Quel collaborateur souhaitez-vous supprimer?")
        return input("ID du collaborateur: ")

    @staticmethod
    def delete_user_warning():
        print("Êtes-vous sûr de vouloir supprimer ce collaborateur?")
        return input("OUI/NON: ")

    @staticmethod
    def management_customers_menu():
        print("\n-----MENU CLIENTS-----")
        print("1) Afficher toutes les fiches clients.")
        print("2) Retour au Menu Commercial.")
        return input("Votre choix: ")

    @staticmethod
    def management_contrats_menu():
        print("\n-----MENU CONTRATS-----")
        print("1) Créer un contrat.")
        print("2) Modifier un contrat.")
        print("3) Afficher tout les contrats.")
        print("4) Retour au Menu Gestion.")
        return input("Votre choix: ")

    @staticmethod
    def id_new_contract():
        print("À partir de quel client souhaitez-vous créer un contrat?")
        return input("ID du client: ")

    @staticmethod
    def id_change_contract():
        print("Quel contrat souhaitez-vous modifier?")
        return input("ID du contrat: ")

    @staticmethod
    def management_events_menu():
        print("\n-----MENU EVENEMENTS-----")
        print("1) Modifier un évènement.")
        print("2) Afficher tout les évènement.")
        print("3) Afficher tous les événements sans supports associés.")
        print("4) Retour au Menu Gestion.")
        return input("Votre choix: ")

    @staticmethod
    def id_change_event():
        print("Quel évènement souhaitez-vous modifier?")
        return input("ID de l'évènement: ")

    @staticmethod
    def new_user_informations():
        print("\n-----NOUVEAU COLLABORATEUR-----")
        user_lastname = input("Nom: ")
        print("\n-----LES DEPARTEMENTS A RESEIGNER:-----")
        print("-----COM: COMMERCIAL-----")
        print("-----GES: GESTION-----")
        print("-----SUP: SUPPORT-----")
        user_department = input("Departement: ")
        user_password = input("Mot de passe: ")
        user_email = input("Email: ")
        return user_lastname, user_department, user_password, user_email

    @staticmethod
    def new_contract_informations():
        print("\n-----NOUVEAU CONTRAT-----")
        contract_sales_id = input("Numéro du commercial associé au contrat: ")
        contract_customer_id = input("Numéro du client associé au contrat: ")
        contract_total_amount = input("Prix total du contrat: ")
        contract_settled_amount = input("Montant déjà réglé: ")
        contract_sign = input("Le contract a-t-il été validé par le client? (Oui=True / Non=False): ")
        return contract_sales_id, contract_customer_id, contract_total_amount, contract_settled_amount, contract_sign

    @staticmethod
    def show_all_events_no_support():
        print("\n---TOUS LES EVENEMENTS SANS SUPPORT ASSOCIE---")
        events = session.query(Event).filter(Event.event_support_id is None).all()
        for event in events:
            print(f"ID: {event.event_id}, Contrat associé: {event.event_contract_id}, "
                  f"Client associé: {event.event_customer_id}, Support associé: {event.event_support_id}, "
                  f"Nom de l'événement: {event.event_title}, Date de début: {event.event_date_start}, "
                  f"Date de fin: {event.event_date_end}, Adresse: {event.event_adress}, "
                  f"Nombre de convives: {event.event_guests}, Notes: {event.event_notes}")

