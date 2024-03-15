from sqlalchemy import or_
from sqlalchemy.orm import aliased

from model.principal import User, Contract, Event, Customer
from database import session

class MainSearch:

    @staticmethod
    def show_all_users(users):
        print("\n---TOUS LES COLLABORATEURS---")
        for user in users:
            print(f"ID: {user.id}, Nom: {user.name_lastname}, Département: {user.department}, Email: {user.email}")

    @staticmethod
    def search_all_users_search():
        print("Recherche avancée parmi l'ID, le nom, le département et l'email.")
        search = input("Recherche: ")
        return search

    @staticmethod
    def show_all_users_search(users):
        print("\n---RESULTAT DE LA RECHERCHE---")
        for user in users:
            print(f"ID: {user.id}, Nom: {user.name_lastname}, Département: {user.department}, Email: {user.email}")

    @staticmethod
    def show_all_customers(customers):
        print("\n---TOUS LES CLIENTS---")
        for customer in customers:
            print(f"ID: {customer.id},  "
                  f"Prénom et nom: {customer.name_lastname}, Email: {customer.email}, "
                  f"Téléphone: {customer.phone}, Nom d'entreprise: {customer.business_name}, "
                  f"Date de premier contact: {customer.date_first_contact}, "
                  f"Dernière mise à jour: {customer.last_date_update}, "
                  f"Vendeur associé: {customer.user.name_lastname},")

    @staticmethod
    def search_all_customers_search():
        print("Recherche avancée parmi l'ID, le nom, l'email le nom d'entreprise et le nom du contact commercial.")
        search = input("Recherche: ")
        return search

    @staticmethod
    def show_all_customers_search(customers):
        print("\n---RESULTAT DE LA RECHERCHE---")
        for customer in customers:
            print(f"ID: {customer.id},  "
                  f"Prénom et nom: {customer.name_lastname}, Email: {customer.email}, "
                  f"Téléphone: {customer.phone}, Nom d'entreprise: {customer.business_name}, "
                  f"Date de premier contact: {customer.date_first_contact}, "
                  f"Dernière mise à jour: {customer.last_date_update}, "
                  f"Vendeur associé: {customer.user.name_lastname},")

    @staticmethod
    def show_all_contracts(contracts):
        print("\n---TOUS LES CONTRATS---")
        for contract in contracts:
            print(f"ID: {contract.id}, Prénom et nom du client: {contract.customer.name_lastname}, "
                  f"Email du client: {contract.customer.email}, Téléphone du client: {contract.customer.phone}, "
                  f"Total du contrat: {contract.total_amount}, "
                  f"Total déjà réglé: {contract.settled_amount}, "
                  f"Total reste à régler: {contract.remaining_amount}, "
                  f"Date de création: {contract.creation_date}, Contrat signé: {contract.contract_sign}, "
                  f"Vendeur associé: {contract.customer.user.name_lastname}")


    @staticmethod
    def search_all_contracts_search():
        print("Recherche avancée parmi l'ID, le nom ou prénom du client, le total du contrat ou le nom prénom du "
              "contact commercial.")
        search = input("Recherche: ")
        return search

    @staticmethod
    def show_all_contracts_search(contracts):
        print("\n---RESULTAT DE LA RECHERCHE---")
        for contract in contracts:
            print(f"ID: {contract.id}, Prénom et nom du client: {contract.customer.name_lastname}, "
                  f"Email du client: {contract.customer.email}, Téléphone du client: {contract.customer.phone}, "
                  f"Total du contrat: {contract.total_amount}, "
                  f"Total déjà réglé: {contract.settled_amount}, "
                  f"Total reste à régler: {contract.remaining_amount}, "
                  f"Date de création: {contract.creation_date}, Contrat signé: {contract.contract_sign}, "
                  f"Vendeur associé: {contract.customer.user.name_lastname}")

    @staticmethod
    def show_all_events(events):
        print("\n---TOUS LES EVENEMENTS---")
        for event in events:
            print(f"ID: {event.id}, Contrat associé: {event.contract_id}, "
                  f"Prénom et nom du client: {event.contract.customer.name_lastname}, "
                  f"Email du client: {event.contract.customer.email}, "
                  f"Téléphone du client: {event.contract.customer.phone}, "
                  f"Nom de l'événement: {event.title}, Date de début: {event.date_hour_start}, "
                  f"Date de fin: {event.date_hour_end}, Adresse: {event.address}, "
                  f"Nombre de convives: {event.guests}, Notes: {event.notes}, "
                  f"Support associé: {event.user.name_lastname if event.user else 'Aucun support'}")

    @staticmethod
    def search_all_events_search():
        print("Recherche avancée parmi l'ID, le nom et prénom du client, le titire de l'événement ou le nom et prénom "
              "du support associé.")
        search = input("Recherche: ")
        return search

    @staticmethod
    def show_all_events_search(events):
        print("\n---RESULTAT DE LA RECHERCHE---")
        for event in events:
            print(f"ID: {event.id}, Contrat associé: {event.contract_id}, "
                  f"Prénom et nom du client: {event.contract.customer.name_lastname}, "
                  f"Email du client: {event.contract.customer.email}, "
                  f"Téléphone du client: {event.contract.customer.phone}, "
                  f"Nom de l'événement: {event.title}, Date de début: {event.date_hour_start}, "
                  f"Date de fin: {event.date_hour_end}, Adresse: {event.address}, "
                  f"Nombre de convives: {event.guests}, Notes: {event.notes}, "
                  f"Support associé: {event.user.name_lastname if event.user else 'Aucun support'}")

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

    @staticmethod
    def message_no_user():
        print("Aucun utilisateur n'a été trouvé!")

    @staticmethod
    def message_no_user_whith_search():
        print("Aucun collaborateur trouvé avec cette recherche.")

    @staticmethod
    def message_no_customer():
        print("Aucun client pour le moment.")

    @staticmethod
    def message_no_customer_whith_search():
        print("Aucun client trouvé avec cette recherche.")

    @staticmethod
    def message_no_contract():
        print("Aucun contrat pour le moment.")

    @staticmethod
    def message_no_contract_whith_search():
        print("Aucun contrat trouvé avec cette recherche.")

    @staticmethod
    def message_no_event():
        print("Aucun événement pour le moment.")

    @staticmethod
    def message_no_event_whith_search():
        print("Aucun événement trouvé avec cette recherche.")