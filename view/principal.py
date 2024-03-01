from sqlalchemy import or_
from model.management import User, Contract, Event, Customer
from database import session

class MainSearch:

    @staticmethod
    def show_all_users():
        print("\n---TOUS LES COLLABORATEURS---")
        users = session.query(User).all()
        for user in users:
            print(f"ID: {user.id}, Nom: {user.name_lastname}, Département: {user.departement}, Email: {user.email}")

    @staticmethod
    def show_all_users_search():
        print("Recherche avancée parmi l'ID, le nom, le département et l'email.")
        search = input("Recherche: ")

        print("\n---RESULTAT DE LA RECHERCHE---")
        users = session.query(User).filter(
            or_(
                User.id == search,
                User.name_lastname.startswith(f"%{search}%"),
                User.department.startswith(f"%{search}%"),
                User.email.startswith(f"%{search}%")
            )
        ).all
        if users:
            for user in users:
                print(f"ID: {user.id}, Nom: {user.name_lastname}, Département: {user.departement}, Email: {user.email}")
        else:
            print("Aucun collaborateur trouvé avec cette recherche.")

    @staticmethod
    def show_all_customers():
        print("\n---TOUS LES CLIENTS---")
        customers = session.query(Customer).all()
        if customers:
            for customer in customers:
                print(f"ID: {customer.id},  "
                      f"Prénom et nom: {customer.name_lastname}, Email: {customer.email}, "
                      f"Téléphone: {customer.phone}, Nom d'entreprise: {customer.bussines_name}, "
                      f"Date de premier contact: {customer.date_first_contact}, "
                      f"Dernière mise à jour: {customer.last_date_update}, "
                      f"Vendeur associé: {customer.sales_contact},")
        else:
            print("Aucun client pour le moment.")

    @staticmethod
    def show_all_customers_search():
        print("Recherche avancée parmi l'ID, le nom, l'email le nom d'entreprise et le nom du contact commercial.")
        search = input("Recherche: ")

        print("\n---RESULTAT DE LA RECHERCHE---")
        customers = session.query(Customer).filter(
            or_(
                Customer.id == search,
                Customer.name_lastname.startswith(f"%{search}%"),
                Customer.email.startswith(f"%{search}%"),
                Customer.bussines_name.startswith(f"%{search}%"),
                Customer.sales_contact.startswith(f"%{search}%")
            )
        ).all
        if customers:
            for customer in customers:
                print(f"ID: {customer.id},  "
                      f"Prénom et nom: {customer.name_lastname}, Email: {customer.email}, "
                      f"Téléphone: {customer.phone}, Nom d'entreprise: {customer.bussines_name}, "
                      f"Date de premier contact: {customer.date_first_contact}, "
                      f"Dernière mise à jour: {customer.last_date_update}, "
                      f"Vendeur associé: {customer.sales_contact},")
        else:
            print("Aucun client trouvé avec cette recherche.")

    @staticmethod
    def show_all_contracts():
        print("\n---TOUS LES CONTRATS---")
        contracts = session.query(Contract).all()
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
            print("Aucun contrat pour le moment.")

    @staticmethod
    def show_all_contracts_search():
        print("Recherche avancée parmi l'ID, le nom ou prénom du client, le total du contrat ou le nom prénom du "
              "contact commercial.")
        search = input("Recherche: ")

        print("\n---RESULTAT DE LA RECHERCHE---")
        contracts = session.query(Contract).filter(
            or_(
                Contract.id == search,
                Contract.customer_name_lastname.startswith(f"%{search}%"),
                Contract.contract_total_amount == search,
                Contract.sales_contact_contract.startswith(f"%{search}%")
            )
        ).all
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
            print("Aucun contrat trouvé avec cette recherche.")

    @staticmethod
    def show_all_events():
        print("\n---TOUS LES EVENEMENTS---")
        events = session.query(Event).all()
        if events:
            for event in events:
                print(f"ID: {event.id}, Contrat associé: {event.contract_id}, "
                      f"Prénom et nom du client: {event.customer_name_lastname}, "
                      f"Email du client: {event.customer_email}, Téléphone du client: {event.customer_phone}, "
                      f"Nom de l'événement: {event.title}, Date de début: {event.date_hour_start}, "
                      f"Date de fin: {event.date_hour_end}, Adresse: {event.adress}, Nombre de convives: {event.guests}, "
                      f"Notes: {event.notes}, Support associé: {event.support_contact}")
        else:
            print("Aucun événement pour le moment.")

    @staticmethod
    def show_all_events_search():
        print("Recherche avancée parmi l'ID, le nom et prénom du client, le titire de l'événement ou le nom et prénom du "
            "support associé.")
        search = input("Recherche: ")

        print("\n---RESULTAT DE LA RECHERCHE---")
        events = session.query(Event).filter(
            or_(
                Event.id == search,
                Event.customer_name_lastname.startswith(f"%{search}%"),
                Event.title.startswith(f"%{search}%"),
                Event.support_contact.startswith(f"%{search}%")
            )
        ).all
        if events:
            for event in events:
                print(f"ID: {event.id}, Contrat associé: {event.contract_id}, "
                      f"Prénom et nom du client: {event.customer_name_lastname}, "
                      f"Email du client: {event.customer_email}, Téléphone du client: {event.customer_phone}, "
                      f"Nom de l'événement: {event.title}, Date de début: {event.date_hour_start}, "
                      f"Date de fin: {event.date_hour_end}, Adresse: {event.adress}, Nombre de convives: {event.guests}, "
                      f"Notes: {event.notes}, Support associé: {event.support_contact}")
        else:
            print("Aucun événement trouvé avec cette recherche.")

class MainView:

    @staticmethod
    def oui_non_input():
        response = input("Oui ou Non?").strip().lower()
        return response

    @staticmethod
    def error_oui_non_input():
        print("Erreur de frappe. Veuillez répondre par 'Oui' ou 'Non'.")

    @staticmethod
    def choise():
        return input("Votre choix: ")