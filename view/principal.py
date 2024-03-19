# This class is used to handle different search views in the application
class MainSearch:
    # This method displays all users
    @staticmethod
    def show_all_users(users):
        print("\n---TOUS LES COLLABORATEURS---")
        for user in users:
            print(f"ID: {user.id}, Nom: {user.name_lastname}, Département: "
                  f"{user.department}, Email: {user.email}")

    # This method handles the advanced search for users
    @staticmethod
    def search_all_users_search():
        print("Recherche avancée parmi l'ID, le nom, le département et "
              "l'email.")
        search = input("Recherche: ")
        return search

    # This method displays the results of the advanced search for users
    @staticmethod
    def show_all_users_search(users):
        print("\n---RESULTAT DE LA RECHERCHE---")
        for user in users:
            print(f"ID: {user.id}, Nom: {user.name_lastname}, Département: "
                  f"{user.department}, Email: {user.email}")

    # This method displays all customers
    @staticmethod
    def show_all_customers(customers):
        print("\n---TOUS LES CLIENTS---")
        for customer in customers:
            print(f"ID: {customer.id},  "
                  f"Prénom et nom: {customer.name_lastname}, Email: "
                  f"{customer.email}, Téléphone: {customer.phone}, "
                  f"Nom d'entreprise: {customer.business_name}, "
                  f"Date de premier contact: {customer.date_first_contact}, "
                  f"Dernière mise à jour: {customer.last_date_update}, "
                  f"Vendeur associé: {customer.user.name_lastname},")

    # This method handles the advanced search for customers
    @staticmethod
    def search_all_customers_search():
        print("Recherche avancée parmi l'ID, le nom, l'email le nom "
              "d'entreprise et le nom du contact commercial.")
        search = input("Recherche: ")
        return search

    # This method displays the results of the advanced search for customers
    @staticmethod
    def show_all_customers_search(customers):
        print("\n---RESULTAT DE LA RECHERCHE---")
        for customer in customers:
            print(f"ID: {customer.id},  "
                  f"Prénom et nom: {customer.name_lastname}, Email: "
                  f"{customer.email}, Téléphone: {customer.phone}, "
                  f"Nom d'entreprise: {customer.business_name}, "
                  f"Date de premier contact: {customer.date_first_contact}, "
                  f"Dernière mise à jour: {customer.last_date_update}, "
                  f"Vendeur associé: {customer.user.name_lastname},")

    # This method displays all contracts
    @staticmethod
    def show_all_contracts(contracts):
        print("\n---TOUS LES CONTRATS---")
        for contract in contracts:
            print(f"ID: {contract.id}, Prénom et nom du client: "
                  f"{contract.customer.name_lastname}, "
                  f"Email du client: {contract.customer.email}, "
                  f"Téléphone du client: {contract.customer.phone}, "
                  f"Total du contrat: {contract.total_amount}, "
                  f"Total déjà réglé: {contract.settled_amount}, "
                  f"Total reste à régler: {contract.remaining_amount}, "
                  f"Date de création: {contract.creation_date}, "
                  f"Contrat signé: {contract.contract_sign}, "
                  f"Vendeur associé: {contract.customer.user.name_lastname}")

    # This method handles the advanced search for contracts
    @staticmethod
    def search_all_contracts_search():
        print("Recherche avancée parmi l'ID, le nom ou prénom du client, le "
              "total du contrat ou le nom prénom du "
              "contact commercial.")
        search = input("Recherche: ")
        return search

    # This method displays the results of the advanced search for contracts
    @staticmethod
    def show_all_contracts_search(contracts):
        print("\n---RESULTAT DE LA RECHERCHE---")
        for contract in contracts:
            print(f"ID: {contract.id}, Prénom et nom du client: "
                  f"{contract.customer.name_lastname}, "
                  f"Email du client: {contract.customer.email}, "
                  f"Téléphone du client: {contract.customer.phone}, "
                  f"Total du contrat: {contract.total_amount}, "
                  f"Total déjà réglé: {contract.settled_amount}, "
                  f"Total reste à régler: {contract.remaining_amount}, "
                  f"Date de création: {contract.creation_date}, "
                  f"Contrat signé: {contract.contract_sign}, "
                  f"Vendeur associé: {contract.customer.user.name_lastname}")

    # This method displays all events
    @staticmethod
    def show_all_events(events):
        print("\n---TOUS LES EVENEMENTS---")
        for event in events:
            print(f"ID: {event.id}, Contrat associé: {event.contract_id}, "
                  f"Prénom et nom du client: "
                  f"{event.contract.customer.name_lastname}, "
                  f"Email du client: {event.contract.customer.email}, "
                  f"Téléphone du client: {event.contract.customer.phone}, "
                  f"Nom de l'événement: {event.title}, "
                  f"Date de début: {event.date_hour_start}, "
                  f"Date de fin: {event.date_hour_end}, "
                  f"Adresse: {event.address}, "
                  f"Nombre de convives: {event.guests}, Notes: {event.notes}, "
                  f"Support associé: "
                  f"{event.user.name_lastname if event.user else 'Aucun'}")

    # This method handles the advanced search for events
    @staticmethod
    def search_all_events_search():
        print("Recherche avancée parmi l'ID, le nom et prénom du client, le "
              "titire de l'événement ou le nom et prénom "
              "du support associé.")
        search = input("Recherche: ")
        return search

    # This method displays the results of the advanced search for events
    @staticmethod
    def show_all_events_search(events):
        print("\n---RESULTAT DE LA RECHERCHE---")
        for event in events:
            print(f"ID: {event.id}, Contrat associé: {event.contract_id}, "
                  f"Prénom et nom du client: "
                  f"{event.contract.customer.name_lastname}, "
                  f"Email du client: {event.contract.customer.email}, "
                  f"Téléphone du client: {event.contract.customer.phone}, "
                  f"Nom de l'événement: {event.title}, "
                  f"Date de début: {event.date_hour_start}, "
                  f"Date de fin: {event.date_hour_end}, "
                  f"Adresse: {event.address}, "
                  f"Nombre de convives: {event.guests}, Notes: {event.notes}, "
                  f"Support associé: "
                  f"{event.user.name_lastname if event.user else 'Aucun'}")

# This class is used to handle different views in the application
class MainView:
    # This method handles the input for yes or no questions
    @staticmethod
    def oui_non_input():
        response = input("Oui ou Non? ").strip().lower()
        return response

    # This method displays an error message for invalid yes or no input
    @staticmethod
    def error_oui_non_input():
        print("Erreur de frappe. Veuillez répondre par 'Oui' ou par 'Non'.")

    # This method handles the input for choices
    @staticmethod
    def choise():
        return input("Votre choix: ")

    # This method displays a message for successful token connection
    @staticmethod
    def message_connection_token():
        print("Connexion réussie avec votre token.")

    # This method displays an error message when the department of a user
    # cannot be retrieved
    @staticmethod
    def message_no_department():
        print("Impossible de récupérer le département de l'utilisateur.")

    # This method displays an error message when the input is not a whole
    # number
    @staticmethod
    def message_no_whole_number():
        print("Veuillez saisir un nombre entier!")

    # This method displays an error message when no user is found
    @staticmethod
    def message_no_user():
        print("Aucun utilisateur n'a été trouvé!")

    # This method displays an error message when no user is found with
    # the search
    @staticmethod
    def message_no_user_whith_search():
        print("Aucun collaborateur trouvé avec cette recherche.")

    # This method displays an error message when no customer is found
    @staticmethod
    def message_no_customer():
        print("Aucun client pour le moment.")

    # This method displays an error message when no customer is found with
    # the search
    @staticmethod
    def message_no_customer_whith_search():
        print("Aucun client trouvé avec cette recherche.")

    # This method displays an error message when no contract is found
    @staticmethod
    def message_no_contract():
        print("Aucun contrat pour le moment.")

    # This method displays an error message when no contract is found with
    # the search
    @staticmethod
    def message_no_contract_whith_search():
        print("Aucun contrat trouvé avec cette recherche.")

    # This method displays an error message when no event is found
    @staticmethod
    def message_no_event():
        print("Aucun événement pour le moment.")

    # This method displays an error message when no event is found with
    # the search
    @staticmethod
    def message_no_event_whith_search():
        print("Aucun événement trouvé avec cette recherche.")
