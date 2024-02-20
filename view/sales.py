from sqlalchemy import and_

from database import session
from model.management import Contract

class SalesMenu:
    @staticmethod
    def sale_menu():
        print(f"\n-----MENU COMMERCIAL-----")
        print("1) Menu clients.")
        print("2) Menu contrats.")
        print("3) Menu evenements.")
        print("4) Quitter la session.")
        return input("Votre choix: ")

    @staticmethod
    def sale_customers_menu():
        print("\n-----MENU CLIENTS-----")
        print("1) Créer une fiche client.")
        print("2) Modifier une fiche client.")
        print("3) Afficher toutes les fiches clients.")
        print("4) Rechercher un client.")
        print("5) Afficher toutes les fiches clients auxquels je suis associé.")
        print("6) Retour au Menu Commercial.")
        return input("Votre choix: ")

    @staticmethod
    def id_change_customer():
        print("Quel client souhaitez-vous modifier?")
        return input("ID du client: ")

    @staticmethod
    def error_customer_not_associated():
        print("Vous n'êtes pas associé à ce client, veuillez en choisir un autre!")

    @staticmethod
    def sale_contracts_menu():
        print("\n-----MENU CONTRATS-----")
        print("1) Modifier un contrat.")
        print("2) Afficher tout les contrats.")
        print("3) Afficher tout mes contrats.")
        print("4) Afficher tous mes contrats non signés.")
        print("5) Afficher tous mes contrats pas entièrement réglés.")
        print("6) Rechercher un contrat.")
        print("7) Retour au Menu Commercial.")
        return input("Votre choix: ")

    @staticmethod
    def id_change_contract():
        print("Quel contrat souhaitez-vous modifier?")
        return input("ID du contrat: ")

    @staticmethod
    def error_contract_not_associated():
        print("Vous n'êtes pas associé à ce contrat, veuillez en choisir un autre!")

    @staticmethod
    def sale_events_menu():
        print("\n-----MENU EVENEMENTS-----")
        print("1) Créer un évènement.")
        print("2) Afficher tout les évènement.")
        print("3) Rechercher un évènement.")
        print("4) Retour au Menu Commercial.")
        return input("Votre choix: ")

    @staticmethod
    def id_new_contract():
        print("À partir de quel contrat souhaitez-vous créer un évènement?")
        return input("ID du contrat: ")

    @staticmethod
    def new_customer_informations():
        print("\n-----NOUVEAU CLIENT-----")
        name_lastname = input("Nom et prénom du client: ")
        email = input("Email du client: ")
        phone = input("Numéro de téléphone du client: ")
        bussines_name = input("Nom de l'entreprise: ")
        return name_lastname, email, phone, bussines_name

    @staticmethod
    def new_event_informations():
        print("\n-----NOUVEL EVENEMENT-----")
        title = input("Intitulé de l'événement: ")
        date_hour_start = input("Date et heure du début de l'événement (format AAAA-MM-DD HH:MM:SS): ")
        date_hour_end = input("Date et heure du fin de l'événement (format AAAA-MM-DD HH:MM:SS): ")
        adress = input("Adresse de l'événement: ")
        guests = input("Nombre d'invités: ")
        notes = input("Notes: ")
        return title, date_hour_start, date_hour_end, adress, guests, notes

    @staticmethod
    def show_my_contracts_not_sign(name_lastname):
        print("\n---TOUS MES CONTRATS NON SIGNÉS---")
        contracts = session.query(Contract).filter(
            and_(
                Contract.sales_contact_contract == name_lastname,
                Contract.contract_sign == False
            )
            ).all()
        if contracts:
            for contract in contracts:
                print(f"ID: {contract.id}, Prénom et nom du client: {contract.customer_name_lastname}, "
                      f"Email du client: {contract.customer_email}, Téléphone du client: {contract.customer_phone}"
                      f"Total du contrat: {contract.contract_total_amount}, "
                      f"Total déjà réglé: {contract.contract_settled_amount}, "
                      f"Total reste à régler: {contract.contract_remaining_amount}, "
                      f"Date de création: {contract.contract_creation_date}, Contrat signé: {contract.contract_sign}, "
                      f"Vendeur associé: {contract.sales_contact_contract}")
        else:
            print("Tous vos contrats ont l'air d'être signés.")

    @staticmethod
    def show_my_contracts_remaining_amount(name_lastname):
        print("\n---TOUS MES CONTRATS NON ENTIÈREMENT RÉGLÉS---")
        contracts = session.query(Contract).filter(
            and_(
                Contract.sales_contact_contract == name_lastname,
                Contract.remaining_amount > 0
            )
        ).all()
        if contracts:
            for contract in contracts:
                print(f"ID: {contract.id}, Prénom et nom du client: {contract.customer_name_lastname}, "
                      f"Email du client: {contract.customer_email}, Téléphone du client: {contract.customer_phone}"
                      f"Total du contrat: {contract.contract_total_amount}, "
                      f"Total déjà réglé: {contract.contract_settled_amount}, "
                      f"Total reste à régler: {contract.contract_remaining_amount}, "
                      f"Date de création: {contract.contract_creation_date}, Contrat signé: {contract.contract_sign}, "
                      f"Vendeur associé: {contract.sales_contact_contract}")
        else:
            print("Tous vos contrats ont l'air totalement réglés.")
