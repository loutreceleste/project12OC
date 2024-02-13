class ManagementMenu:
    @staticmethod
    def management_menu(self):
        print(f"\n-----BONJOUR {self.lastname}-----")
        print("1) Menu collaborateurs.")
        print("1) Menu clients.")
        print("2) Menu contrats.")
        print("3) Menu evenements.")
        print("4) Quitter la session.")
        return input("Votre choix: ")

    @staticmethod
    def management_users_menu():
        print("\n-----MENU COLLABORATEURS-----")
        print("1) Créer un collaborateur.")
        print("2) Modifier un collaborateur.")
        print("3) Supprimer un collaborateur.")
        print("4) Afficher tout les collaborateurs.")
        print("5) Retour au Menu Gestion.")
        return input("Votre choix: ")

    @staticmethod
    def management_contrats_menu():
        print("\n-----MENU CONTRATS-----")
        print("1) Créer un contrat.")
        print("2) Modifier un contrat.")
        print("3) Afficher tout les contrats.")
        print("4) Retour au Menu Gestion.")
        return input("Votre choix: ")

    @staticmethod
    def management_events_menu():
        print("\n-----MENU EVENEMENTS-----")
        print("1) Modifier un évènement.")
        print("2) Afficher tout les évènement.")
        print("3) Afficher tous les événements sans supports associés.")
        print("4) Retour au Menu Gestion.")
        return input("Votre choix: ")

    @staticmethod
    def new_user_informations():
        print("\n-----NOUVEAU COLLABORATEUR-----")
        user_lastname = input("Nom: ")
        print("\n-----LES DEPARTEMENTS A RESEIGNER:-----")
        print("-----COM: COMMERCIAL-----")
        print("-----GES: GESTION-----")
        print("-----SUP: SUPPORT-----")
        user_department = input("Departement: ")
        user_password = input("Mot de passe: ")
        user_email = input("Email: ")
        return user_lastname, user_department, user_password, user_email

    @staticmethod
    def new_contract_informations():
        print("\n-----NOUVEAU CONTRAT-----")
        contract_sales_id = input("Numéro du commercial associé au contrat: ")
        contract_customer_id = input("Numéro du contrat associé au contrat: ")
        contract_total_amount = input("Prix total du contrat: ")
        contract_settled_amount = input("Montant déjà réglé: ")
        contract_sign = input("Le contract a-t-il été validé par le client? (Oui=True / Non=False): ")
        return contract_sales_id, contract_customer_id, contract_total_amount, contract_settled_amount, contract_sign
