from sqlalchemy import or_
from model.management import User, Contract, Event
from model.sales import Customer
from database import session

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
    def show_all_users():
        print("\n---TOUS LES COLLABORATEURS---")
        users = session.query(User).all()
        for user in users:
            print(f"ID: {user.user_id}, Nom: {user.user_lastname}, Département: {user.user_departement},"
                  f"Email: {user.user_email}")

    @staticmethod
    def search_users_input():
        print("Recherche avancée parmi l' ID, le nom, le département et l'email.")
        return input("Recherche: ")

    @staticmethod
    def show_all_users_search(search):
        print("\n---RESULTAT DE LA RECHERCHE---")
        users = session.query(User).filter(
            or_(
                User.user_id == search,
                User.user_lastname.startswith(f"%{search}%"),
                User.user_department.startswith(f"%{search}%"),
                User.user_email.startswith(f"%{search}%")
            )
        ).all
        if users:
            for user in users:
                print(f"ID: {user.user_id}, Nom: {user.user_lastname}, Département: {user.user_departement},"
                      f"Email: {user.user_email}")
            else:
                print("Aucun collaborateur trouvé avec cette recherche.")

    @staticmethod
    def show_all_customers():
        print("\n---TOUS LES CLIENTS---")
        customers = session.query(Customer).all()
        if customers:
            for customer in customers:
                print(f"ID: {customer.customer_id}, Vendeur associé: {customer.customer_sales_id}, "
                      f"Nom: {customer.customer_lastname}, Email: {customer.customer_email}, "
                      f"Téléphone: {customer.customer_phone}, Nom d'entreprise: {customer.customer_bussines_name}, "
                      f"Date de premier contact: {customer.customer__date_first_contact}, "
                      f"Dernière mise à jour: {customer.customer_last_update}, "
                      f"Contact événement: {customer.customer_event_contact}")
        else:
            print("Aucun client pour le moment.")

    @staticmethod
    def search_customers_input():
        print("Recherche avancée parmi l'ID, le nom, l'email et le nom d'entreprise.")
        return input("Recherche: ")

    @staticmethod
    def show_all_customers_search(search):
        print("\n---RESULTAT DE LA RECHERCHE---")
        customers = session.query(Customer).filter(
            or_(
                Customer.customer_id == search,
                Customer.customer_lastname.startswith(f"%{search}%"),
                Customer.customer_email.startswith(f"%{search}%"),
                Customer.customer_bussines_name.startswith(f"%{search}%")
            )
        ).all
        if customers:
            for customer in customers:
                print(f"ID: {customer.customer_id}, Vendeur associé: {customer.customer_sales_id}, "
                      f"Nom: {customer.customer_lastname}, Email: {customer.customer_email}, "
                      f"Téléphone: {customer.customer_phone}, Nom d'entreprise: {customer.customer_bussines_name}, "
                      f"Date de premier contact: {customer.customer__date_first_contact}, "
                      f"Dernière mise à jour: {customer.customer_last_update}, "
                      f"Contact événement: {customer.customer_event_contact}")
            else:
                print("Aucun client trouvé avec cette recherche.")

    @staticmethod
    def show_all_contracts():
        print("\n---TOUS LES CONTRATS---")
        contracts = session.query(Contract).all()
        if contracts:
            for contract in contracts:
                print(f"ID: {contract.contract_id}, Vendeur associé: {contract.contract_sales_id}, "
                      f"Client associé: {contract.contract_customer_id}, Total du contrat: {contract.contract_total_amount}, "
                      f"Total déjà réglé: {contract.contract_settled_amount}, "
                      f"Total reste à régler: {contract.contract_remaining_amount}, "
                      f"Date de création: {contract.contract_creation_date}, Contrat signé: {contract.contract_sign}")
        else:
            print("Aucun contrat pour le moment.")

    @staticmethod
    def search_contracts_input():
        print("Recherche avancée parmi l'ID, le montant total ou l'ID du commercial associé.")
        return input("Recherche: ")

    @staticmethod
    def show_all_contracts_search(search):
        print("\n---RESULTAT DE LA RECHERCHE---")
        contracts = session.query(Contract).filter(
            or_(
                Contract.contract_id == search,
                Contract.contract_customer_id == search,
                Contract.contract_total_amount == search,
                Contract.contract_sales_id == search,
            )
        ).all
        if contracts:
            for contract in contracts:
                print(f"ID: {contract.contract_id}, Vendeur associé: {contract.contract_sales_id}, "
                      f"Client associé: {contract.contract_customer_id}, Total du contrat: {contract.contract_total_amount}, "
                      f"Total déjà réglé: {contract.contract_settled_amount}, "
                      f"Total reste à régler: {contract.contract_remaining_amount}, "
                      f"Date de création: {contract.contract_creation_date}, Contrat signé: {contract.contract_sign}")
            else:
                print("Aucun contrat trouvé avec cette recherche.")

    @staticmethod
    def show_all_events():
        print("\n---TOUS LES EVENEMENTS---")
        events = session.query(Event).all()
        if events:
            for event in events:
                print(f"ID: {event.event_id}, Contrat associé: {event.event_contract_id}, "
                      f"Client associé: {event.event_customer_id}, Support associé: {event.event_support_id}, "
                      f"Nom de l'événement: {event.event_title}, Date de début: {event.event_date_start}, "
                      f"Date de fin: {event.event_date_end}, Adresse: {event.event_adress}, "
                      f"Nombre de convives: {event.event_guests}, Notes: {event.event_notes}")
        else:
            print("Aucun événement pour le moment.")

    @staticmethod
    def search_events_input():
        print("Recherche avancée parmi l'ID, le montant total ou l'ID du commercial associé.")
        return input("Recherche: ")

    @staticmethod
    def show_all_events_search(search):
        print("\n---RESULTAT DE LA RECHERCHE---")
        events = session.query(Event).filter(
            or_(
                Event.event_id == search,
                Event.event_title.startswith(f"%{search}%"),
                Event.event_customer_id == search
            )
        ).all
        if events:
            for event in events:
                print(f"ID: {event.event_id}, Contrat associé: {event.event_contract_id}, "
                      f"Client associé: {event.event_customer_id}, Support associé: {event.event_support_id}, "
                      f"Nom de l'événement: {event.event_title}, Date de début: {event.event_date_start}, "
                      f"Date de fin: {event.event_date_end}, Adresse: {event.event_adress}, "
                      f"Nombre de convives: {event.event_guests}, Notes: {event.event_notes}")
            else:
                print("Aucun événement trouvé avec cette recherche.")
