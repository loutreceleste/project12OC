# This class is used to display different menus for the sales module
class SalesMenu:
    # This method displays the main commercial menu
    @staticmethod
    def sale_menu():
        print("\n-----MENU COMMERCIAL-----")
        print("1) Menu clients.")
        print("2) Menu contrats.")
        print("3) Menu evenements.")
        print("4) Quitter la session.")

    # This method displays the customers sub-menu
    @staticmethod
    def sale_customers_menu():
        print("\n-----MENU CLIENTS-----")
        print("1) Créer une fiche client.")
        print("2) Modifier une fiche client.")
        print("3) Afficher toutes les fiches clients.")
        print("4) Rechercher un client.")
        print("5) Afficher toutes les fiches clients auxquels je suis "
              "associé.")
        print("6) Retour au Menu Commercial.")

    # This method displays the contracts sub-menu
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

    # This method displays the events sub-menu
    @staticmethod
    def sale_events_menu():
        print("\n-----MENU EVENEMENTS-----")
        print("1) Créer un évènement.")
        print("2) Afficher tout les évènement.")
        print("3) Rechercher un évènement.")
        print("4) Retour au Menu Commercial.")

# This class is used to display different search views for the sales module
class SalesSearchViews:
    # This method displays all customers associated with the current user
    @staticmethod
    def show_my_customers(customers):
        print("\n---TOUS MES CLIENTS---")
        for customer in customers:
            print(f"ID: {customer.id},  "
                  f"Prénom et nom: {customer.name_lastname}, "
                  f"Email: {customer.email}, "
                  f"Téléphone: {customer.phone}, "
                  f"Nom d'entreprise: {customer.business_name}, "
                  f"Date de premier contact: {customer.date_first_contact}, "
                  f"Dernière mise à jour: {customer.last_date_update}, "
                  f"Vendeur associé: {customer.user.name_lastname},")

    # This method displays all contracts associated with the current user
    @staticmethod
    def show_my_contracts(contracts):
        print("\n---TOUS MES CONTRATS---")
        for contract in contracts:
            print(f"ID: {contract.id}, Prénom et nom du client: "
                  f"{contract.customer.name_lastname}, "
                  f"Email du client: {contract.customer.email}, "
                  f"Téléphone du client: {contract.customer.phone}"
                  f"Total du contrat: {contract.total_amount}, "
                  f"Total déjà réglé: {contract.settled_amount}, "
                  f"Total reste à régler: {contract.remaining_amount}, "
                  f"Date de création: {contract.creation_date}, "
                  f"Contrat signé: {contract.contract_sign}, "
                  f"Vendeur associé: {contract.customer.user.name_lastname}")

    # This method displays all unsigned contracts associated with the
    # current user
    @staticmethod
    def show_my_contracts_not_sign(contracts):
        print("\n---TOUS MES CONTRATS NON SIGNÉS---")
        for contract in contracts:
            print(f"ID: {contract.id}, Prénom et nom du client: "
                  f"{contract.customer.name_lastname}, "
                  f"Email du client: {contract.customer.email}, "
                  f"Téléphone du client: {contract.customer.phone}"
                  f"Total du contrat: {contract.total_amount}, "
                  f"Total déjà réglé: {contract.settled_amount}, "
                  f"Total reste à régler: {contract.remaining_amount}, "
                  f"Date de création: {contract.creation_date}, "
                  f"Contrat signé: {contract.contract_sign}, "
                  f"Vendeur associé: {contract.customer.user.name_lastname}")

    # This method displays all not fully paid contracts associated with the
    # current user
    @staticmethod
    def show_my_contracts_remaining_amount(contracts):
        print("\n---TOUS MES CONTRATS NON ENTIÈREMENT RÉGLÉS---")
        for contract in contracts:
            print(f"ID: {contract.id}, Prénom et nom du client: "
                  f"{contract.customer.name_lastname}, "
                  f"Email du client: {contract.customer.email}, "
                  f"Téléphone du client: {contract.customer.phone}"
                  f"Total du contrat: {contract.total_amount}, "
                  f"Total déjà réglé: {contract.settled_amount}, "
                  f"Total reste à régler: {contract.remaining_amount}, "
                  f"Date de création: {contract.creation_date}, "
                  f"Contrat signé: {contract.contract_sign}, "
                  f"Vendeur associé: {contract.customer.user.name_lastname}")

# This class is used to handle different views related to customers in the
# sales module
class SalesCustomerViews:
    # This method handles the view to create a new customer
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

    # This method handles the view to update an existing customer
    @staticmethod
    def update_customer_view(customer):
        print(f"\n-----MISE A JOUR DU CLIENT N°{customer.id}-----")
        print("Appuyez sur 'Entrée' afin de conserver l'information actuelle.")
        name_lastname = input(f"Nom et prénom du client "
                              f"({customer.name_lastname}): ")
        email = input(f"Email du client ({customer.email}): ")
        while True:
            phone_input = input(f"Téléphone du client ({customer.phone}): ")
            if phone_input.strip() == "":
                phone = customer.phone
                break
            elif phone_input.isdigit():
                phone = int(phone_input)
                break
            else:
                print("Veuillez indiquer un numéro de téléphone.")
        business_name = input(f"Nom commercial du client "
                              f"({customer.business_name}): ")
        return name_lastname, email, phone, business_name

    # This method displays a message when a customer is successfully created
    @staticmethod
    def validation_customer_creation():
        print("Votre client a été créé avec succès!")

    # This method handles the view to get the ID of the customer to be updated
    @staticmethod
    def update_customer_id_view():
        print("Quel client souhaitez vous modifier?")
        id = input("ID du client à modifier: ")
        return id

    # This method displays a message when a customer is successfully updated
    @staticmethod
    def validation_update_customer_view():
        print("La fiche de votre client a bien été modifié!")

    # This method displays a message when the current user is not in charge
    # of a customer
    @staticmethod
    def not_in_charge_customer_view():
        print("Vous n'êtes pas en change de ce client.")

    # This method displays a message when no customer is found
    @staticmethod
    def none_customer_view():
        print("Erreur de frappe ou aucun client ne correspond a cette ID.")

    # This method displays a message when the date format is incorrect
    @staticmethod
    def wrong_date_format():
        print("Le format de la date est incorrect, veuillez réessayer.")

    # This method displays a message when the current user has no contracts
    @staticmethod
    def no_contract_view():
        print("Vous n'avez aucun contrat pour le moment.")

    # This method displays a message when all contracts of the current user
    # are signed
    @staticmethod
    def all_contract_sign_view():
        print("Tous vos contrats ont l'air d'être signés.")

    # This method displays a message when all contracts of the current user
    # are fully paid
    @staticmethod
    def all_contract_settled():
        print("Tous vos contrats ont l'air totalement réglés.")
