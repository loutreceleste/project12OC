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
    def sale_events_menu():
        print("\n-----MENU EVENEMENTS-----")
        print("1) Créer un évènement.")
        print("2) Afficher tout les évènement.")
        print("3) Rechercher un évènement.")
        print("4) Retour au Menu Commercial.")
        return input("Votre choix: ")

class SalesSearchViews:

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

class SalesCustomerViews:

    @staticmethod
    def create_customer_view():
        print("\n-----NOUVEAU CLIENT-----")
        name_lastname = input("Nom et prénom du client: ")
        email = input("Email du client: ")
        while True:
            phone = input("Téléphone du client: ")
            if phone.isdigit():
                phone = int(phone)
                break
            else:
                print("Veuillez indiquer un numéro de téléphone.")
        bussines_name = input("Nom commercial du client: ")
        return name_lastname, email, phone, bussines_name

    @staticmethod
    def validation_customer_creation():
        print("Votre client a été créé avec succès!")

    @staticmethod
    def update_customer_id_view():
        print("Quel client souhaitez vous modifier?")
        id = input("ID du cleint a modifier: ")
        return id

    @staticmethod
    def update_customer_view(customer):
        print(f"\n-----MISE A JOUR DU CLIENT N°{customer.id}-----")
        name_lastname = input(f"Nom et prénom du client: {customer.name_lastname}")
        email = input(f"Email du client: {customer.email}")
        while True:
            phone = input(f"Téléphone du client: {customer.phone}")
            if phone == int:
                break
            else:
                print("Veuillez indiquer un numéro de téléphone.")
        bussines_name = input(f"Nom commercial du client: {customer.bussines_name}")
        return name_lastname, email, phone, bussines_name

    @staticmethod
    def validation_update_customer_view():
        print("La fiche de votre client a bien été modifié!")

    @staticmethod
    def not_in_charge_customer_view():
        print("Vous n'êtes pas en change de ce client. Vous allez être redirigé vers le Menu Commercial.")

    @staticmethod
    def none_customer_view():
        print("Erreur de frappe ou aucun client ne correspond a cette ID. Vous allez être redirigé vers le "
              "Menu Commercial.")
