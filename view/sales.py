class SalesMenu:
    @staticmethod
    def sale_menu(self):
        print(f"\n-----BONJOUR {self.lastname}-----")
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
        print("4) Retour au Menu Commercial.")
        return input("Votre choix: ")

    @staticmethod
    def sale_contrats_menu():
        print("\n-----MENU CONTRATS-----")
        print("1) Modifier un contrat.")
        print("2) Afficher tout les contrats.")
        print("3) Afficher tous les contrats non signés.")
        print("4) Afficher tous les contrats pas entièrement réglés.")
        print("5) Retour au Menu Commercial.")
        return input("Votre choix: ")

    @staticmethod
    def sale_events_menu():
        print("\n-----MENU EVENEMENTS-----")
        print("1) Créer un évènement.")
        print("2) Afficher tout les évènement.")
        print("3) Retour au Menu Commercial.")
        return input("Votre choix: ")

    @staticmethod
    def new_customer_informations():
        print("\n-----NOUVEAU CLIENT-----")
        customer_lastname = input("Nom du client: ")
        customer_email = input("Email du client: ")
        customer_phone = input("Numéro de téléphone du client: ")
        customer_bussines_name = input("Nom de l'entreprise: ")
        customer_event_contact = input("Contact pour les événements: ")
        return customer_lastname, customer_email, customer_phone, customer_bussines_name, customer_event_contact

    @staticmethod
    def new_event_informations():
        print("\n-----NOUVEL EVENEMENT-----")
        event_contract_id = input("Numéro du contrat associé à l'événement: ")
        event_customer_id = input("Numéro du client associé à l'événement: ")
        event_support_id = input("Numéro du support associé à l'événement: ")
        event_title = input("Intitulé de l'événement: ")
        event_date_start = input("Date et heure du début de l'événement (format AAAA-MM-DD HH:MM:SS): ")
        event_date_end = input("Date et heure du fin de l'événement (format AAAA-MM-DD HH:MM:SS): ")
        event_adress = input("Adresse de l'événement: ")
        event_guests = input("Nombre d'invités: ")
        event_notes = input("Notes: ")
        return (event_contract_id, event_customer_id, event_support_id, event_title, event_date_start, event_date_end,
                event_adress, event_guests, event_notes)
