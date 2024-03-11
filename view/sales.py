from sqlalchemy import and_

from database import session



class SalesMenu:
    @staticmethod
    def sale_menu():
        print(f"\n-----MENU COMMERCIAL-----")
        print("1) Menu clients.")
        print("2) Menu contrats.")
        print("3) Menu evenements.")
        print("4) Quitter la session.")

    @staticmethod
    def sale_customers_menu():
        print("\n-----MENU CLIENTS-----")
        print("1) Créer une fiche client.")
        print("2) Modifier une fiche client.")
        print("3) Afficher toutes les fiches clients.")
        print("4) Rechercher un client.")
        print("5) Afficher toutes les fiches clients auxquels je suis associé.")
        print("6) Retour au Menu Commercial.")

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

    @staticmethod
    def sale_events_menu():
        print("\n-----MENU EVENEMENTS-----")
        print("1) Créer un évènement.")
        print("2) Afficher tout les évènement.")
        print("3) Rechercher un évènement.")
        print("4) Retour au Menu Commercial.")

class SalesSearchViews:

    @staticmethod
    def show_my_customers(user):
        from model.principal import Customer
        print("\n---TOUS MES CLIENTS---")
        customers = session.query(Customer).filter(Customer.sales_contact == user.id).all()
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
    def show_my_contracts(user):
        from model.principal import Contract
        from model.principal import Customer
        print("\n---TOUS MES CONTRATS---")
        contracts = session.query(Contract).join(Contract.customer).join(Customer.user).filter(Contract.id == user.id).all()
        if contracts:
            for contract in contracts:
                print(f"ID: {contract.id}, Prénom et nom du client: {contract.customer_name_lastname}, "
                      f"Email du client: {contract.customer_email}, Téléphone du client: {contract.customer_phone}"
                      f"Total du contrat: {contract.contract_total_amount}, "
                      f"Total déjà réglé: {contract.contract_settled_amount}, "
                      f"Total reste à régler: {contract.contract_remaining_amount}, "
                      f"Date de création: {contract.contract_creation_date}, Contrat signé: {contract.contract_sign}, "
                      f"Vendeur associé: {Contract.customer.user.name_lastname}")
        else:
            print("Vous n'avez aucun contrat pour le moment.")

    @staticmethod
    def show_my_contracts_not_sign(user):
        from model.principal import Contract
        from model.principal import Customer
        from model.principal import User
        print("\n---TOUS MES CONTRATS NON SIGNÉS---")
        contracts = session.query(Contract).join(Contract.customer).join(Customer.user).filter(
            and_(
                User.id == user.id,
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
                      f"Vendeur associé: {Contract.customer.user.name_lastname}")
        else:
            print("Tous vos contrats ont l'air d'être signés.")

    @staticmethod
    def show_my_contracts_remaining_amount(user):
        from model.principal import Contract
        from model.principal import Customer
        from model.principal import User
        print("\n---TOUS MES CONTRATS NON ENTIÈREMENT RÉGLÉS---")
        contracts = session.query(Contract).join(Contract.customer).join(Customer.user).filter(
            and_(
                User.id == user.id,
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
                      f"Vendeur associé: {Contract.customer.user.name_lastname}")
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
        id = input("ID du client à modifier: ")
        return id

    @staticmethod
    def update_customer_view(customer):
        print(f"\n-----MISE A JOUR DU CLIENT N°{customer.id}-----")
        print("Appuyez sur 'Entrée' afin de conserver l'information actuelle.")
        name_lastname = input(f"Nom et prénom du client: ({customer.name_lastname})")
        email = input(f"Email du client: ({customer.email})")
        while True:
            phone_input = input(f"Téléphone du client: ({customer.phone})")
            if phone_input.strip() == "":
                phone = customer.phone
                break
            elif phone_input.isdigit():
                phone = int(phone_input)
                break
            else:
                print("Veuillez indiquer un numéro de téléphone.")
        business_name = input(f"Nom commercial du client: ({customer.business_name})")
        return name_lastname, email, phone, business_name

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

    @staticmethod
    def choise():
        return input("Votre choix: ")
