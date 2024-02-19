from database import session
from model.management import Event, User


class ManagementMenu:
    @staticmethod
    def management_menu():
        print(f"\n-----MENU GESTION-----")
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
        print("2) Rechercher un client.")
        print("3) Retour au Menu Gestion.")
        return input("Votre choix: ")

    @staticmethod
    def management_contrats_menu():
        print("\n-----MENU CONTRATS-----")
        print("1) Créer un contrat.")
        print("2) Modifier un contrat.")
        print("3) Afficher tout les contrats.")
        print("4) Rechercher un contrat.")
        print("5) Retour au Menu Gestion.")
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
        print("3) Rechercher un évènement.")
        print("4) Afficher tous les événements sans supports associés.")
        print("5) Retour au Menu Gestion.")
        return input("Votre choix: ")

    @staticmethod
    def id_change_event():
        print("Quel évènement souhaitez-vous modifier?")
        return input("ID de l'évènement: ")

    @staticmethod
    def new_user_informations():
        print("\n-----NOUVEAU COLLABORATEUR-----")
        name_lastname = input("Nom et prénom: ")
        print("\n-----LES DEPARTEMENTS A RESEIGNER:-----")
        print("-----COM: COMMERCIAL-----")
        print("-----GES: GESTION-----")
        print("-----SUP: SUPPORT-----")
        department = input("Departement: ")
        password = input("Mot de passe: ")
        email = input("Email: ")
        return name_lastname, department, password, email

    @staticmethod
    def new_contract_informations():
        print("\n-----NOUVEAU CONTRAT-----")
        total_amount = input("Cout total du contrat: ")
        settled_amount = input("Montant déjà réglé: ")
        contract_sign = input("Le contract a-t-il été validé par le client? (Oui=True / Non=False): ")
        return total_amount, settled_amount, contract_sign

    @staticmethod
    def show_all_events_no_support():
        print("\n---TOUS LES EVENEMENTS SANS SUPPORT ASSOCIE---")
        events = session.query(Event).filter(Event.support_contact is None).all()
        for event in events:
            print(f"ID: {event.id}, Contrat associé: {event.contract_id}, "
                  f"Client associé: {event.event_customer_id}, Support associé: {event.event_support_id}, "
                  f"Nom de l'événement: {event.event_title}, Date de début: {event.event_date_start}, "
                  f"Date de fin: {event.event_date_end}, Adresse: {event.event_adress}, "
                  f"Nombre de convives: {event.event_guests}, Notes: {event.event_notes}")

