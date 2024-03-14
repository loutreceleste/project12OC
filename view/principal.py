from sqlalchemy import or_
from sqlalchemy.orm import aliased

from model.principal import User, Contract, Event, Customer
from database import session

class MainSearch:

    @staticmethod
    def show_all_users():
        print("\n---TOUS LES COLLABORATEURS---")
        users = session.query(User).all()
        for user in users:
            print(f"ID: {user.id}, Nom: {user.name_lastname}, Département: {user.department}, Email: {user.email}")

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
        ).all()
        if users:
            for user in users:
                print(f"ID: {user.id}, Nom: {user.name_lastname}, Département: {user.department}, Email: {user.email}")
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
                      f"Téléphone: {customer.phone}, Nom d'entreprise: {customer.business_name}, "
                      f"Date de premier contact: {customer.date_first_contact}, "
                      f"Dernière mise à jour: {customer.last_date_update}, "
                      f"Vendeur associé: {customer.user.name_lastname},")
        else:
            print("Aucun client pour le moment.")

    @staticmethod
    def show_all_customers_search():
        print("Recherche avancée parmi l'ID, le nom, l'email le nom d'entreprise et le nom du contact commercial.")
        search = input("Recherche: ")

        user_alias = aliased(User)

        print("\n---RESULTAT DE LA RECHERCHE---")
        customers = session.query(Customer).join(user_alias).filter(
            or_(
                Customer.id == search,
                Customer.name_lastname.startswith(f"%{search}%"),
                Customer.email.startswith(f"%{search}%"),
                Customer.business_name.startswith(f"%{search}%"),
                user_alias.name_lastname.startswith(f"%{search}%")
            )
        ).all()
        if customers:
            for customer in customers:
                print(f"ID: {customer.id},  "
                      f"Prénom et nom: {customer.name_lastname}, Email: {customer.email}, "
                      f"Téléphone: {customer.phone}, Nom d'entreprise: {customer.business_name}, "
                      f"Date de premier contact: {customer.date_first_contact}, "
                      f"Dernière mise à jour: {customer.last_date_update}, "
                      f"Vendeur associé: {customer.user.name_lastname},")
        else:
            print("Aucun client trouvé avec cette recherche.")

    @staticmethod
    def show_all_contracts():
        print("\n---TOUS LES CONTRATS---")
        customer_alias = aliased(Customer)
        user_alias = aliased(User)

        contracts = session.query(Contract). \
            join(customer_alias, Contract.customer_id == customer_alias.id). \
            join(user_alias, customer_alias.sales_contact == user_alias.id).all()

        if contracts:
            for contract in contracts:
                print(f"ID: {contract.id}, Prénom et nom du client: {contract.customer.name_lastname}, "
                      f"Email du client: {contract.customer.email}, Téléphone du client: {contract.customer.phone}, "
                      f"Total du contrat: {contract.total_amount}, "
                      f"Total déjà réglé: {contract.settled_amount}, "
                      f"Total reste à régler: {contract.remaining_amount}, "
                      f"Date de création: {contract.creation_date}, Contrat signé: {contract.contract_sign}, "
                      f"Vendeur associé: {contract.customer.user.name_lastname}")
        else:
            print("Aucun contrat pour le moment.")

    @staticmethod
    def show_all_contracts_search():
        print("Recherche avancée parmi l'ID, le nom ou prénom du client, le total du contrat ou le nom prénom du "
              "contact commercial.")
        search = input("Recherche: ")

        print("\n---RESULTAT DE LA RECHERCHE---")
        customer_alias = aliased(Customer)
        user_alias = aliased(User)

        contracts = session.query(Contract). \
            join(customer_alias, Contract.customer_id == customer_alias.id). \
            join(user_alias, customer_alias.sales_contact == user_alias.id).filter(
            or_(
                Contract.id == search,
                customer_alias.name_lastname.startswith(f"%{search}%"),
                Contract.total_amount == search,
                user_alias.name_lastname.startswith(f"%{search}%")
            )
        ).all()
        if contracts:
            for contract in contracts:
                print(f"ID: {contract.id}, Prénom et nom du client: {contract.customer.name_lastname}, "
                      f"Email du client: {contract.customer.email}, Téléphone du client: {contract.customer.phone}, "
                      f"Total du contrat: {contract.total_amount}, "
                      f"Total déjà réglé: {contract.settled_amount}, "
                      f"Total reste à régler: {contract.remaining_amount}, "
                      f"Date de création: {contract.creation_date}, Contrat signé: {contract.contract_sign}, "
                      f"Vendeur associé: {contract.customer.user.name_lastname}")
        else:
            print("Aucun contrat trouvé avec cette recherche.")

    @staticmethod
    def show_all_events():
        print("\n---TOUS LES EVENEMENTS---")
        contract_alias = aliased(Contract)
        customer_alias = aliased(Customer)
        user_alias = aliased(User)

        events = session.query(Event).join(contract_alias, Event.contract). \
            join(customer_alias, contract_alias.customer).outerjoin(user_alias, Event.user).all()
        if events:
            for event in events:
                print(f"ID: {event.id}, Contrat associé: {event.contract_id}, "
                      f"Prénom et nom du client: {event.contract.customer.name_lastname}, "
                      f"Email du client: {event.contract.customer.email}, "
                      f"Téléphone du client: {event.contract.customer.phone}, "
                      f"Nom de l'événement: {event.title}, Date de début: {event.date_hour_start}, "
                      f"Date de fin: {event.date_hour_end}, Adresse: {event.address}, "
                      f"Nombre de convives: {event.guests}, Notes: {event.notes}, "
                      f"Support associé: {event.user.name_lastname if event.user else 'Aucun support'}")
        else:
            print("Aucun événement pour le moment.")

    @staticmethod
    def show_all_events_search():
        print("Recherche avancée parmi l'ID, le nom et prénom du client, le titire de l'événement ou le nom et prénom "
              "du support associé.")
        search = input("Recherche: ")

        print("\n---RESULTAT DE LA RECHERCHE---")
        contract_alias = aliased(Contract)
        customer_alias = aliased(Customer)
        user_alias = aliased(User)

        events = (session.query(Event).join(contract_alias, Event.contract).
                  join(customer_alias, contract_alias.customer).outerjoin(user_alias, Event.user).filter(
            or_(
                Event.id == search,
                customer_alias.name_lastname.startswith(f"%{search}%"),
                Event.title.startswith(f"%{search}%"),
                user_alias.name_lastname.startswith(f"%{search}%")
            )
        ).all())
        if events:
            for event in events:
                print(f"ID: {event.id}, Contrat associé: {event.contract_id}, "
                      f"Prénom et nom du client: {event.contract.customer.name_lastname}, "
                      f"Email du client: {event.contract.customer.email}, "
                      f"Téléphone du client: {event.contract.customer.phone}, "
                      f"Nom de l'événement: {event.title}, Date de début: {event.date_hour_start}, "
                      f"Date de fin: {event.date_hour_end}, Adresse: {event.address}, "
                      f"Nombre de convives: {event.guests}, Notes: {event.notes}, "
                      f"Support associé: {event.user.name_lastname if event.user else 'Aucun support'}")
        else:
            print("Aucun événement trouvé avec cette recherche.")

class MainView:

    @staticmethod
    def oui_non_input():
        response = input("Oui ou Non? ").strip().lower()
        return response

    @staticmethod
    def error_oui_non_input():
        print("Erreur de frappe. Veuillez répondre par 'Oui' ou par 'Non'.")

    @staticmethod
    def choise():
        return input("Votre choix: ")

    @staticmethod
    def message_connection_token():
        print("Connexion réussie avec votre token.")

    @staticmethod
    def message_no_department():
        print("Impossible de récupérer le département de l'utilisateur.")

    @staticmethod
    def message_no_whole_number():
        print("Veuillez saisir un nombre entier!")
